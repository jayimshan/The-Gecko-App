from PyQt5.QtCore import QObject, pyqtSignal, QByteArray
from PyQt5 import QtCore, QtNetwork
from bs4 import BeautifulSoup
from webhook import Webhook
from webview import Webview

import gecko_utils

import json
import time
import requests
import random
import urllib.parse
import webpage

class Funkoshop(QObject):

	update_product_image = pyqtSignal(str)
	update_product_title = pyqtSignal(str)
	update_product_size = pyqtSignal(str)
	update_task_status = pyqtSignal(str)
	update_task_log = pyqtSignal(str)

	store = 'https://shop.funko.com/'
	base_url = 'https://shop.funko.com'
	url_products = 'https://shop.funko.com/products.json'
	url_product = 'https://shop.funko.com/products/'
	url_add_js = 'https://shop.funko.com/cart/add.js'
	# url_cart_js = 'https://shop.funko.com/cart.js'
	url_cart = 'https://shop.funko.com/cart/'
	url_shipping_rates = 'https://shop.funko.com/cart/shipping_rates.json'
	url_payment_gateway_endpoint = 'https://deposit.us.shopifycs.com/sessions'
	url_start_checkout = 'https://shop.funko.com/checkout'
	url_wallets = 'https://shop.funko.com/10522158/digital_wallets/dialog'
	payment_gateway = 126896850

	capture_folder = 'store_funkoshop_test'

	headers = {
		'authority': 'shop.funko.com',
		'method': 'GET',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7,pt;q=0.6',
		'origin': 'https://shop.funko.com',
		'referer': 'https://shop.funko.com/',
		'upgrade-insecure-requests': '1',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
		'x-requested-with': 'XMLHttpRequest'
	}

	def __init__(self, task_type, captcha_logic, keywords, qty, size, color, profile, billing):
		super().__init__()
		self.title = None
		self.src = None
		self.variant_id = None
		self.price = None
		self.shipping_rate = None
		self.direct_link = None
		self.shipping_code = None
		self.sitekey = None

		self.s = requests.Session()
		self.task_type = task_type
		self.captcha_logic = captcha_logic
		self.keywords = keywords
		self.qty = qty
		self.size = size
		self.color = color
		self.profile = profile
		self.billing = billing
		self.token = None
		
		self.cookies = []
		self.resolution = gecko_utils.get_random_client_resolution()
		self.waiting_for_captcha = False
		self.browser_is_available = False
		self.rendered_html = None
		self.abort = False
		self.auth_token = None
		self.url_checkout = None
		self.url_step = None

		self.status = {
			'captcha_detected': False,
			'search_all_products': False,
			'add_to_cart': False,
			'start_checkout': False,
			'submit_info': False,
			'submit_shipping': False,
			'submit_payment': False,
			'checkout_successful': False
		}

	def detect_captcha(self, html):
		if self.captcha_logic == QtCore.Qt.Unchecked:
			print('    [CAPTCHA]: Ignoring')
		else:
			if gecko_utils.detect_captcha(html):
				self.status['captcha_detected'] = True
				self.sitekey = gecko_utils.get_sitekey(html)

		self.cookies = []
		for cookie in self.s.cookies:
			c = QtNetwork.QNetworkCookie()
			c.setDomain(cookie.__dict__['domain'])
			c.setName(bytes(cookie.__dict__['name'], 'utf-8'))
			c.setValue(bytes(cookie.__dict__['value'], 'utf-8'))
			self.cookies.append(c)

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
		print('Adding to cart')
		payload = json.dumps({
			'items': [
				{
					'quantity': self.qty,
					'id': self.variant_id
				}
			]
		})
		post_headers = self.headers
		post_headers['content-type'] = 'application/json'
		# post_headers['content-type'] = 'application/x-www-form-urlencoded'
		post_headers['method'] = 'POST'
		r = self.s.post(self.url_add_js, headers=post_headers, data=payload, proxies=proxy).json()
		gecko_utils.capture_response(self.capture_folder, 'cart_object.json', r)
		# print('[CART]: {}'.format(r))
		if r['items']:
			self.price = r['items'][0]['final_line_price'] * 0.01
			print('    [PRICE]: ${0:.2f}'.format(self.price))
			return True
		else:
			return False

	def start_checkout(self, proxy=None):
		print('Starting checkout')
		r = self.s.get(self.url_start_checkout, headers=self.headers, proxies=proxy)
		self.url_checkout = r.url.split('?')[0]
		print('    [CHECKOUT URL]: {}'.format(self.url_checkout))
		self.url_step = r.url
		print('    [STEP]: {}'.format(r.url))
		soup = BeautifulSoup(r.text, 'html.parser')
		gecko_utils.capture_response(self.capture_folder, 'start_checkout.html', soup.prettify())
		title = str(soup.find('title'))
		print('    [TITLE]: {}'.format(title))
		self.auth_token = soup.find('input', {'name': 'authenticity_token'})['value']
		print('    [AUTH TOKEN]: {}'.format(self.auth_token))
		self.detect_captcha(r.text)
		if 'error' not in title.lower():
			return True
		else:
			return False

	def submit_info(self, proxy=None):
		print('Submitting info')

		print('    [G-RECAPTCHA-RESPONSE]: {}'.format(self.token))

		payload = [
			('_method', 'patch'),
			('authenticity_token', self.auth_token),
			('previous_step', 'contact_information'),
			('step', 'shipping_method'),
			('checkout[email]', self.profile.email),
			('checkout[buyer_accepts_marketing]', 0),
			('checkout[buyer_accepts_marketing]', 1),
			('checkout[shipping_address][first_name]', ''),
			('checkout[shipping_address][last_name]', ''),
			('checkout[shipping_address][company]', ''),
			('checkout[shipping_address][address1]', ''),
			('checkout[shipping_address][address2]', ''),
			('checkout[shipping_address][city]', ''),
			('checkout[shipping_address][country]', ''),
			('checkout[shipping_address][province]', ''),
			('checkout[shipping_address][zip]', ''),
			('checkout[shipping_address][first_name]', self.profile.first_name),
			('checkout[shipping_address][last_name]', self.profile.last_name),
			('checkout[shipping_address][company]', ''),
			('checkout[shipping_address][address1]', self.profile.shipping_address),
			('checkout[shipping_address][address2]', self.profile.shipping_address_2),
			('checkout[shipping_address][city]', self.profile.shipping_city),
			('checkout[shipping_address][country]', 'United States'),
			('checkout[shipping_address][province]', self.profile.shipping_state),
			('checkout[shipping_address][zip]', self.profile.shipping_zip),
			('checkout[remember_me]', 'false'),
			('checkout[remember_me]', 0),
			('g-recaptcha-response', self.token),
			('checkout[client_details][browser_width]', self.resolution['width']),
			('checkout[client_details][browser_height]', self.resolution['height']),
			('checkout[client_details][javascript_enabled]', 1),
			('checkout[client_details][color_depth]', 24),
			('checkout[client_details][java_enabled]', 'false'),
			('checkout[client_details][browser_tz]', 240)
		]

		post_headers = self.headers
		post_headers['content-type'] = 'application/x-www-form-urlencoded'
		post_headers['method'] = 'POST'
		r = self.s.post(self.url_checkout, headers=post_headers, data=payload, proxies=proxy)
		self.url_step = r.url
		print('    [STEP]: {}'.format(r.url))
		soup = BeautifulSoup(r.text, 'html.parser')
		gecko_utils.capture_response(self.capture_folder, 'submit_info.html', soup.prettify())
		title = str(soup.find('title'))
		print('    [TITLE]: {}'.format(title))
		self.auth_token = soup.find('input', {'name': 'authenticity_token'})['value']
		print('    [AUTH TOKEN]: {}'.format(self.auth_token))
		self.detect_captcha(r.text)
		if 'error' not in title.lower():
			return True
		else:
			return False

	def submit_shipping(self, proxy=None):
		print('Submitting shipping')
		# self.shipping_code = soup.find('input', {'name': 'checkout[shipping_rate][id]'})['value']
		# self.shipping_code = self.get_shipping_rates(self.url_shipping_rates, self.profile, proxy)
		self.shipping_details = gecko_utils.get_shipping_rates(self.s, self.url_shipping_rates, self.profile, self.headers, proxy)
		print('    [SHIPPING DETAILS]')
		print('        [SOURCE]: {}'.format(self.shipping_details['source']))
		print('        [CODE]: {}'.format(self.shipping_details['code']))
		print('        [PRICE]: {}'.format(self.shipping_details['price']))
		print('        [SHIPPING CODE]: {}'.format(self.shipping_details['shipping_code']))
		payload = {
			'_method': 'patch',
			'authenticity_token': self.auth_token,
			'previous_step': 'shipping_method',
			'step': 'payment_method',
			'checkout[shipping_rate][id]': self.shipping_details['shipping_code'],
			'checkout[client_details][browser_width]': self.resolution['width'],
			'checkout[client_details][browser_height]': self.resolution['height'],
			'checkout[client_details][javascript_enabled]': 1,
			'checkout[client_details][color_depth]': 24,
			'checkout[client_details][java_enabled]': 'false',
			'checkout[client_details][browser_tz]': 240
		}
		post_headers = self.headers
		post_headers['content-type'] = 'application/x-www-form-urlencoded'
		post_headers['method'] = 'POST'
		r = self.s.post(self.url_checkout, headers=post_headers, data=payload, proxies=proxy)
		self.url_step = r.url
		print('    [STEP]: {}'.format(r.url))
		soup = BeautifulSoup(r.text, 'html.parser')
		gecko_utils.capture_response(self.capture_folder, 'submit_shipping.html', soup.prettify())
		title = str(soup.find('title'))
		print('    [TITLE]: {}'.format(title))
		self.auth_token = soup.find('input', {'name': 'authenticity_token'})['value']
		print('    [AUTH TOKEN]: {}'.format(self.auth_token))
		self.detect_captcha(r.text)
		if 'error' not in title.lower():
			return True
		else:
			return False

	def submit_payment(self, proxy=None):
		print('Submitting payment')

		subtotal = self.price + float(self.shipping_details['price'])
		checkout_price = gecko_utils.get_checkout_price(subtotal, self.profile.shipping_zip)
		session_id = gecko_utils.get_session_id(self.billing)

		if self.profile.same_as_shipping == QtCore.Qt.Checked:
			print('    [SAME AS SHIPPING]: TRUE')
			payload = {
				'_method': 'patch',
				'authenticity_token': self.auth_token,
				'previous_step': 'payment_method',
				'step': '',
				's': session_id,
				'checkout[payment_gateway]': self.payment_gateway,
				'checkout[credit_card][vault]': 'false',
				'checkout[different_billing_address]': 'false',
				'checkout[total_price]': checkout_price,
				'complete': 1,
				'checkout[client_details][browser_width]': self.resolution['width'],
				'checkout[client_details][browser_height]': self.resolution['height'],
				'checkout[client_details][javascript_enabled]': 1,
				'checkout[client_details][color_depth]': 24,
				'checkout[client_details][java_enabled]': 'false',
				'checkout[client_details][browser_tz]': 240
			}
		else:
			print('    [SAME AS SHIPPING]: FALSE')
			payload = {
				'_method': 'patch',
				'authenticity_token': self.auth_token,
				'previous_step': 'payment_method',
				'step': '',
				's': session_id,
				'checkout[payment_gateway]': self.payment_gateway,
				'checkout[credit_card][vault]': 'false',
				'checkout[different_billing_address]': 'true',
				'checkout[billing_address][first_name]': self.profile.first_name,
				'checkout[billing_address][last_name]': self.profile.last_name,
				'checkout[billing_address][company]': '',
				'checkout[billing_address][address1]': self.profile.billing_address,
				'checkout[billing_address][address2]': self.profile.billing_address_2,
				'checkout[billing_address][city]': self.profile.billing_city,
				'checkout[billing_address][country]': 'United States',
				'checkout[billing_address][province]': self.profile.billing_state,
				'checkout[billing_address][zip]': self.profile.billing_zip,
				'checkout[total_price]': checkout_price,
				'complete': 1,
				'checkout[client_details][browser_width]': self.resolution['width'],
				'checkout[client_details][browser_height]': self.resolution['height'],
				'checkout[client_details][javascript_enabled]': 1,
				'checkout[client_details][color_depth]': 24,
				'checkout[client_details][java_enabled]': 'false',
				'checkout[client_details][browser_tz]': 240
			}

		post_headers = self.headers
		post_headers['content-type'] = 'application/x-www-form-urlencoded'
		post_headers['method'] = 'POST'

		self.s.post(self.url_checkout, headers=post_headers, data=payload, proxies=proxy)
		r = self.s.get(self.url_wallets, headers=self.headers, proxies=proxy)
		soup = BeautifulSoup(r.text, 'html.parser')
		gecko_utils.capture_response(self.capture_folder, 'submit_payment.html', soup.prettify())
		title = str(soup.find('title'))
		if 'error' in title.lower():
			self.update_task_status.emit('Payment error')
			return False
		else:
			return True

	def verify_checkout(self):
		try:
			webhook = Webhook(self.title, self.store, self.direct_link, self.price, self.qty, self.src, self.color, self.size_emit)
		except Exception as e:
			print(str(e))
		finally:
			return True
