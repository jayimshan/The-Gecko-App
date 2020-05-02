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
import threading

class Vogmask(QObject):

	update_product_image = pyqtSignal(str)
	update_product_title = pyqtSignal(str)
	update_product_size = pyqtSignal(str)
	update_task_status = pyqtSignal(str)
	update_task_log = pyqtSignal(str)

	request_render = pyqtSignal()
	captcha_detected = pyqtSignal()
	request_poll_token = pyqtSignal()

	store = 'https://www.vogmask.com/'
	url_products = 'http://www.vogmask.com/products.json'
	url_product = 'https://www.vogmask.com/products/'
	url_add_js = 'https://www.vogmask.com/cart/add.js'
	url_cart_js = 'https://www.vogmask.com/cart.js'
	url_cart = 'https://www.vogmask.com/cart/'
	url_payment_gateway_endpoint = 'https://deposit.us.shopifycs.com/sessions'
	url_checkout = 'https://www.vogmask.com/checkout'
	url_wallets = 'https://www.vogmask.com/2500840/digital_wallets/dialog'
	url_step = None
	payment_gateway = 33832337502
	headers = {
		'authority': 'www.vogmask.com',
		'method': 'GET',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7,pt;q=0.6',
		'origin': 'https://www.vogmask.com',
		'referer': 'https://www.vogmask.com/',
		'upgrade-insecure-requests': '1',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
		'x-requested-with': 'XMLHttpRequest'
	}

	lock = threading.Lock()

	def __init__(self, s, task_type, captcha_logic, keywords, qty, size, color, profile, billing):
		QObject.__init__(self)

		self.title = None
		self.src = None
		self.variant_id = None
		self.price = None
		self.direct_link = None
		self.authenticity_token = None
		self.shipping_code = None
		self.checkout_price = None

		self.s = s
		self.task_type = task_type
		self.captcha_logic = captcha_logic
		self.keywords = keywords
		self.qty = qty
		self.size = size
		self.color = color
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

	def random_client_resolution(self):
		self.client_width = random.randint(800, 1921)
		self.client_height = random.randint(600, 1081)
		print('Client Window Resolution: {}x{}'.format(self.client_width, self.client_height))

	def render_page(self):
		self.page.set_cookies(self.cookies)
		self.page.loadFinished.connect(self.set_html)
		self.page.load(QtCore.QUrl(self.url_step))

	def set_html(self):
		self.page.page.toHtml(self.callable)

	def callable(self, data):
		self.page.html = data

	def rendering_page(self):
		while self.page.html is None:
			if self.abort:
				self.page.stop()
				return False
			else:
				time.sleep(0.1)
		return True

	def detect_captcha(self, soup):
		if self.captcha_logic == QtCore.Qt.Unchecked:
			print('Ignoring captcha')
		elif self.captcha_logic == QtCore.Qt.PartiallyChecked or self.captcha_logic == QtCore.Qt.Checked:
			captcha = soup.find('textarea', id='g-recaptcha-response')
			if captcha:
				self.captcha_detected.emit()
				self.waiting_for_captcha = True
				while self.waiting_for_captcha:
					print('Polling for token')
					self.request_poll_token.emit()
					time.sleep(0.5)
			else:
				print("No captcha detected")
		else:
			print('Error with logic')

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
				except requests.exceptions.ProxyError as e:
					print('[EXCEPTION] {}'.format(e))
					self.update_task_status.emit('Proxy error')
					return False
				except Exception as e:
					print('[EXCEPTION] {}'.format(e))
					return False

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
			self.update_product_title.emit(self.title)
			self.update_product_image.emit(self.src)
			if self.search_for_size(product['variants']):
				self.update_product_size.emit(self.size_emit)
				# self.update_status(self.title, self.src, self.size_emit)
				self.direct_link = '{}{}'.format(self.url_product, product['handle'])
				return True
			else:
				self.update_task_status.emit('Size unavailable')
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
		return False

	def update_status(self, title, src, size):
		self.update_product_title.emit(title)
		self.update_product_image.emit(src)
		self.update_product_size.emit(size)

	def add_to_cart(self, proxy=None):
		payload = {
			# 'form_type': 'product',
			# 'utf8': '✓',
			'id': self.variant_id,
			'quantity': self.qty,
			# 'add': ''
		}
		post_headers = self.headers
		post_headers['content-type'] = 'application/x-www-form-urlencoded'
		post_headers['method'] = 'POST'
		r = self.s.post(self.url_add_js, headers=post_headers, data=payload, proxies=proxy)
		r = self.s.get(self.url_cart_js, headers=self.headers, proxies=proxy)
		cart = r.json()
		print(cart)
		if len(cart['items']) > 0:
			# Carted
			self.price = cart['items'][0]['final_line_price']
			return True
		else:
			# Unsuccessful
			return False

	def start_checkout(self, proxy=None):
		payload = {
			'updates[]': 1,
			'checkout': 'PROCEED TO CHECKOUT'
		}
		post_headers = self.headers
		post_headers['content-type'] = 'application/x-www-form-urlencoded'
		post_headers['method'] = 'POST'
		r = self.s.post(self.url_cart, headers=post_headers, data=payload, proxies=proxy)
		# print('Start checkout url: {}'.format(r.url))
		self.url_step = r.url.split('?')[0]
		soup = BeautifulSoup(r.text, 'html.parser')
		title = soup.find('title')
		# print(title)
		tokens = soup.find_all('input', {'name': 'authenticity_token'})
		# print('Tokens: {}'.format(len(tokens)))
		self.authenticity_token = tokens[0]['value']
		# print(self.authenticity_token)
		self.detect_captcha(soup)
		if 'error' not in str(title).lower():
			return True
		else:
			return False

	def submit_info(self, proxy=None):
		# print('Submitting info')

		payload = [
			('_method', 'patch'),
			('authenticity_token', self.authenticity_token),
			('previous_step', 'contact_information'),
			('step', 'payment_method'),
			('checkout[email_or_phone]', self.profile.email),
			('checkout[buyer_accepts_marketing]', 0),
			('checkout[billing_address][first_name]', ''),
			('checkout[billing_address][last_name]', ''),
			('checkout[billing_address][company]', ''),
			('checkout[billing_address][address1]', ''),
			('checkout[billing_address][address2]', ''),
			('checkout[billing_address][city]', ''),
			('checkout[billing_address][country]', ''),
			('checkout[billing_address][province]', ''),
			('checkout[billing_address][zip]', ''),
			('checkout[billing_address][phone]', ''),
			('checkout[billing_address][first_name]', self.profile.first_name),
			('checkout[billing_address][last_name]', self.profile.last_name),
			('checkout[billing_address][company]', ''),
			('checkout[billing_address][address1]', self.profile.shipping_address),
			('checkout[billing_address][address2]', self.profile.shipping_address_2),
			('checkout[billing_address][city]', self.profile.shipping_city),
			('checkout[billing_address][country]', 'United States'),
			('checkout[billing_address][province]', self.profile.shipping_state),
			('checkout[billing_address][zip]', self.profile.shipping_zip),
			('checkout[billing_address][phone]', ''),
			('checkout[client_details][browser_width]', self.client_width),
			('checkout[client_details][browser_height]', self.client_height),
			('checkout[client_details][javascript_enabled]', 1),
			('checkout[client_details][color_depth]', 24),
			('checkout[client_details][java_enabled]', 'false'),
			('checkout[client_details][browser_tz]', 300)
		]

		post_headers = self.headers
		post_headers['content-type'] = 'application/x-www-form-urlencoded'
		post_headers['method'] = 'POST'
		r = self.s.post(self.url_step, headers=post_headers, data=payload, proxies=proxy)
		# self.url_checkout = r.url

		self.cookies = []
		for cookie in self.s.cookies:
			c = QtNetwork.QNetworkCookie()
			c.setDomain(cookie.__dict__['domain'])
			c.setName(bytes(cookie.__dict__['name'], 'utf-8'))
			c.setValue(bytes(cookie.__dict__['value'], 'utf-8'))
			self.cookies.append(c)

		self.request_render.emit()
		if not self.rendering_page():
			return False

		soup = BeautifulSoup(self.page.html, 'html.parser')
		tokens = soup.find_all('input', {'name': 'authenticity_token'})
		self.checkout_price = soup.find('input', {'id': 'checkout_total_price'})['value']
		print('Checkout price: {}'.format(self.checkout_price))
		print('Tokens: {}'.format(len(tokens)))
		self.authenticity_token = tokens[0]['value']
		title = soup.find('title')
		print(title)
		if 'error' not in str(title).lower():
			return True
		else:
			return False

	def submit_shipping(self, proxy=None):
		# print('Submitting shipping')
		return True

	def submit_payment(self, proxy=None):
		# print('Submitting payment')
		card = '{} {} {} {}'.format(self.billing.card_number[:4], self.billing.card_number[4:8], self.billing.card_number[8:12], self.billing.card_number[12:])
		# print(card)

		payload = {
			'credit_card': {
				'number': card,
				'name': self.billing.name_on_card,
				'month': self.billing.exp_month,
				'year': self.billing.exp_year,
				'verification_value': self.billing.cvv
			}
		}
		headers = {
			'accept': 'application/json',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7,pt;q=0.6',
			'content-type': 'application/json',
			'host': 'deposit.us.shopifycs.com',
			'origin': 'https://checkout.us.shopifycs.com',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
		}
		# url = '{}{}'.format(self.base_url, self.url_checkout)
		r = self.s.post(self.url_payment_gateway_endpoint, headers=headers, data=json.dumps(payload), proxies=proxy)
		data = r.json()
		session_id = data['id']
		# print('Session ID: {}'.format(session_id))
		payload = {
			'_method': 'patch',
			'authenticity_token': self.authenticity_token,
			'previous_step': 'payment_method',
			'step': '',
			's': session_id,
			'checkout[payment_gateway]': self.payment_gateway,
			'checkout[credit_card][vault]': 'false',
			'checkout[total_price]': self.checkout_price,
			'complete': 1,
			'checkout[client_details][browser_width]': self.client_width,
			'checkout[client_details][browser_height]': self.client_height,
			'checkout[client_details][javascript_enabled]': 1,
			'checkout[client_details][color_depth]': 24,
			'checkout[client_details][java_enabled]': 'false',
			'checkout[client_details][browser_tz]': 300
		}
		post_headers = self.headers
		post_headers['content-type'] = 'application/x-www-form-urlencoded'
		post_headers['method'] = 'POST'

		r = self.s.post(self.url_step, headers=post_headers, data=payload, proxies=proxy)
		r = self.s.get(self.url_wallets, headers=self.headers, proxies=proxy)
		# print(r.text)
		# self.url_checkout = r.url
		# print(r.status_code)
		# print(r.text)
		soup = BeautifulSoup(r.text, 'html.parser')
		title = soup.find('title')
		if 'error' in str(title).lower():
			self.update_task_status.emit('Payment declined')
			return False
		else:
			return True

	def verify_checkout(self):
		try:
			webhook = Webhook(self.title, self.store, self.direct_link, self.price, self.qty, self.src, self.color, self.size)
		except Exception as e:
			print(str(e))
		finally:
			return True