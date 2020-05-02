from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import QtCore, QtNetwork
from bs4 import BeautifulSoup
from webhook import Webhook
from webpage import Webpage

import requests
import random
import json
import time
import urllib.parse

class Paniniamerica(QObject):

	url_add = 'https://api.paniniamerica.net/onepanini'
	headers = {
		'authority': 'www.paniniamerica.net',
		'method': 'GET',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7,pt;q=0.6',
		'upgrade-insecure-requests': '1',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
	}

	# s = requests.Session()

	def __init__(self, s, task_type, captcha_logic, keywords, size, qty, profile, billing):
		QObject.__init__(self)
		self.title = None
		self.src = None
		self.variant_id = None
		self.authenticity_token = None
		self.shipping_code = None
		self.checkout_price = None

		self.s = s
		self.task_type = task_type
		self.captcha_logic = captcha_logic
		self.keywords = keywords
		self.size = size
		self.qty = qty
		self.profile = profile
		self.billing = billing
		self.token = None
		self.size_emit = None
		
		self.page = Webpage()
		self.cookies = []
		self.client_width = None
		self.client_height = None
		self.random_client_resolution()
		self.waiting_for_captcha = False
		self.abort = False

		self.status = {
			'search_all_products': False,
			'add_to_cart': False,
			'start_checkout': False,
			'submit_info': False,
			'submit_shipping': False,
			'submit_payment': False,
			'checkout_successful': False
		}

	# Get all products
	def search_all_products(self, proxy=None):
		# print('Searching for product')
		limit = 250
		page = 1
		while True:
			if self.abort:
				return False
			else:
				url = '{}?limit={}&page={}'.format(self.url_products, limit, page)
				try:
					r = self.s.get(url, headers=self.headers, proxies=proxy)
				except requests.exceptions.ProxyError as e:
					print('[EXCEPTION] {}'.format(e))
					self.update_task_status.emit('Proxy error')
					return False
				except Exception as e:
					print('[EXCEPTION] {}'.format(e))
					return False
				cache = r.headers['x-cache']
				# print('cache: {}'.format(cache))
				data = json.loads(r.text)
				product_count = len(data['products'])
				# print('products: {}'.format(product_count))
				if product_count > 0:
					for p in data['products']:
						if self.abort:
							return False
						else:
							if self.search_for_product(p): return True
					if product_count < limit:
						return False
				else:
					return False
				page += 1

	# Search for matching product
	def search_for_product(self, product):
		title = product['title']
		image_url = product['images'][0]['src']
		if all(kw in title.lower() for kw in self.keywords['pos']):
			if self.keywords['neg']:
				if any(kw in title.lower() for kw in self.keywords['neg']):
					return False

			self.title = title
			self.src = image_url
			if self.search_for_size(product['variants']):
				self.update_status(self.title, self.src, self.size_emit)
				return True
			else:
				return False
		else:
			return False

	# Search for size/variant
	def search_for_size(self, variants):
		if self.size == 'N/A':
			self.variant_id = variants[0]['id']
			self.size_emit = self.size
			return True
		elif self.size == 'Any':
			variant_count = len(variants)
			random_size = random.randint(0, variant_count)
			self.variant_id = variants[random_size]['id']
			self.size_emit = variants[random_size]['title']
			return True
		else:
			for variant in variants:
				if self.size.lower() in variant['title'].lower():
					self.variant_id = variant['id']
					self.size_emit = variant['title']
					return True
				else:
					return False

	def update_status(self, title, src, size):
		self.update_product_title.emit(title)
		self.update_product_image.emit(src)
		self.update_product_size.emit(size)