import requests
import json

import gecko_utils

class BestBuyCA:

	def __init__(self):

		self.s = requests.Session()

		self.headers = {
			'accept': '*/*',
			'accept-encoding': 'gzip, deflate, br',
			'accept-lanugage': 'en-CA',
			'host': 'www.bestbuy.ca',
			'origin': 'https://www.bestbuy.ca',
			'content-type': 'application/json',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
			'postal-code': 'M5G 2C3',
			'region-code': 'ON'
		}

		self.sku = '12601650'
		self.qty = 1
		self.cart_id = None
		self.line_item_type = None
		self.offer_id = None
		self.name = None
		self.seller_id = None
		self.total_purchase_price = None
		self.tx = None
		self.shipping_id = None

		self.line_id = None
		self.token = None
		self.redirect_url = None
		self.order_id = None
		self.threeDS = None
		self.public_key = None
		self.key_id = None

#--------------------CONFIRMED--------------------

	def add_to_cart(self):
		print('Adding to cart')
		url = 'https://www.bestbuy.ca/api/basket/v2/baskets'
		payload = {
			'lineItems': [{
				'sku': self.sku,
				'quantity': self.qty
			}]
		}
		r = self.s.post(url, headers=self.headers, json=payload)
		print(r)
		data = r.json()
		self.cart_id = data['id']
		self.line_item_type = data['shipments'][0]['lineItems'][0]['lineItemType']
		self.offer_id = data['shipments'][0]['lineItems'][0]['sku']['offer']['id']
		self.name = data['shipments'][0]['lineItems'][0]['sku']['product']['name']
		self.seller_id = data['shipments'][0]['seller']['id']
		self.total_purchase_price = data['shipments'][0]['lineItems'][0]['totalPurchasePrice']
		print(data)
		# print(self.offer_id)
		# print(self.name)
		# print(self.seller_id)
		# print(self.total_purchase_price)

	def get_basket(self):
		print('Getting basket')
		url = f'https://www.bestbuy.ca/api/basket/v2/baskets/{self.cart_id}'
		r = self.s.get(url, headers=self.headers)
		print(r)
		data = r.json()
		print(data)

	def checkout(self):
		print('Starting checkout')
		url = 'https://www.bestbuy.com/cart/d/checkout'
		h = self.headers
		h['X-ORDER-ID'] = self.cart_id
		payload = {}
		r = self.s.post(url, headers=h, json=payload)
		print(r)
		print(r.url)
		data = r.json()
		print(data)
		self.token = data['updateData']['order']['ciaToken']
		print(self.token)
		self.redirect_url = data['updateData']['redirectUrl']
		print(self.redirect_url)

	def sign_in_as_guest(self):
		print('Signing in as guest')
		url = 'https://www.bestbuy.ca/identity/global/signin'
		params = {
			'redirectUrl': 'https://www.bestbuy.ca/checkout/?qit=1#/en-ca/shipping/ON/M5G 2C3',
			'lang': 'en-CA',
			'contextId': 'checkout'
		}
		r = self.s.get(url, headers=self.headers, params=params)
		print(r)
		print(r.url)
		for cookie in self.s.cookies:
			if cookie.name == 'tx':
				self.tx = cookie.value
		print(self.tx)

	def post_shipping(self):
		print('Posting shipping')
		url = 'https://www.bestbuy.ca/api/checkout/checkout/orders'
		h = self.headers
		h['X-TX'] = self.tx
		payload = {
			'email': 'semajhan@gmail.com',
			'lineItems': [{
				'lineItemType': self.line_item_type,
				'name': self.name,
				'offerId': self.offer_id,
				'quantity': self.qty,
				'sellerId': self.seller_id,
				'sku': self.sku,
				'total': self.total_purchase_price
			}],
			'shippingAddress': {
				'address': '480 Progress Ave',
				'apartmentNumber': '',
				'city': 'Scarborough',
				'country': 'CA',
				'firstName': 'Jamie',
				'lastName': 'Lee',
				'phones': [{
					'ext': '',
					'phone': '4162967020'
				}],
				'postalCode': 'M1P 5J1',
				'province': 'ON'
			}
		}
		r = self.s.post(url, headers=h, json=payload)
		print(r)
		data = r.json()
		print(data)
		self.shipping_id = data['id']

	def get_key(self):
		print('Getting key')
		url = 'https://www.bestbuy.ca/ch/config.json'
		r = self.s.get(url, headers=self.headers)
		print(r)
		data = r.json()
		print(data)
		self.public_key = data['encryption']['publicKey']
		self.key_id = data['encryption']['terminalNo']

	def put_payment(self):
		print('Putting payment')
		number = gecko_utils.get_encrypted_card(self.public_key, '483313003762', self.key_id, ca=True)
		# print(type(number))
		url = f'https://www.bestbuy.ca/api/checkout/checkout/orders/{self.shipping_id}/payments'
		h = self.headers
		h['accept'] = 'application/vnd.bestbuy.checkout+json'
		h['X-TX'] = self.tx
		payload = {
			'email': 'semajhan@gmail.com',
			'payment': {
				'creditCard': {
					'billingAddress': {
						'address': '480 Progress Ave',
						'apartmentNumber': '',
						'city': 'Scarborough',
						'country': 'CA',
						'firstName': 'Jamie',
						'lastName': 'Holland',
						'phones': [{
							'ext': '',
							'phone': '4162967020'
						}],
						'postalCode': 'M1P 5J1',
						'province': 'ON'
					},
					'cardNumber': number,
					# '12/v8UpTTKDLh0WtlU1MT7M7hT7tTMAS2vKX8cWQivjnOONlyW15OgzeVHvNy3K6mUT66WCWEogahpXJV8Y5ur/KWL8r10oi5djCecxxz12OF2O7bXpb3mKZzcAk/Wn5S1cOHr9S+0zbUOxwKb1pAnEuPB8ZGdPPHFV+CZ19rpH7GLhTk5YCB5lqTauje1ecp3F3ZA2Q44ylzT5vGISTzWX0HNH2Bk5/LJAkkKe53fsKWoiKhfDLOfgsRGStS3xiD3x8LsxmyVi7vr3XSP6qmJY9LPrXkNajaMCXpRbQQ13D8pRIKP7XEChFqLlpS+LgJGCbcmSsk1l5gXv29lDtjA==8039',
					'cardType': 'VISA',
					'cvv': '530',
					'expirationMonth': '09',
					'expirationYear': '2020'
				}
			}
		}
		r = self.s.put(url, headers=h, json=payload)
		print(r)
		data = r.json()
		print(data)
		# d = data['paymentMethodSummary']['creditCardSummary']['secureAccountRegistration']
		# self.bank_param = d['bankParameters']
		# self.md = d['orderId']
		# self.term_url = d['termUrl']

	def post_redirect(self):
		url = 'https://0eaf.cardinalcommerce.com/EAFService/jsp/v1/redirect'
		h = self.headers
		h['content-type'] = 'application/x-www-form-urlencoded'
		payload = {
			'PaReq': self.bank_param,
			'MD': self.md,
			'TermUrl': self.term_url
		}
		r = self.s.post(url, headers=self.headers, data=payload)
		print(r)
		print(r.text)

	def prelookup(self):
		print('Getting prelookup')
		url = 'https://www.bestbuy.com/payment/api/v1/threeDSecure/preLookup'
		h = self.headers
		h['X-CLIENT'] = 'CHECKOUT'
		payload = {
			'binNumber': '483313',
			'browserInfo': {
				'colorDepth': '24',
				'height': '1920',
				'width': '1080',
				'javaEnabled': 'false',
				'language': 'en-US',
				'timeZone': '240',
				'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'
			},
			'orderId': self.order_id
		}
		r = self.s.post(url, headers=h, json=payload)
		print(r)
		data = r.json()
		print(data)
		self.threeDS = data['threeDSReferenceId']

	def submit_payment(self):
		print('Submitting payment')
		url = 'https://www.bestbuy.ca/api/checkout/checkout/orders/submit'
		h = self.headers
		h['X-TX'] = self.tx
		payload = {
			'cvv': '410',
			'email': 'semajhan@gmail.com',
			'id': self.shipping_id,
			'secureAuthenticationResponse': '',
			'totalPurchasePrice': 90.39
		}
		r = self.s.post(url, headers=h, json=payload)
		print(r)
		data = r.json()
		print(data)

	def verify_payment(self):
		url = f'https://www.bestbuy.com/checkout/orders/{self.cart_id}/'
		h = self.headers
		h['X-User-Interface'] = 'DotCom-Optimized'
		payload = {
			'browserInfo': {
				'colorDepth': '24',
				'height': '1920',
				'width': '1080',
				'javaEnabled': 'false',
				'language': 'en-US',
				'timeZone': '240',
				'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'
			}
		}
		r = self.s.post(url, headers=h, json=payload)
		print(r)
		print(r.url)
		data = r.json()
		print(data)
		state = data['state']
		if 'submitted' in state.lower():
			print('Checked Out!')

	#--------------------TESTING--------------------

	def get_cart(self):
		url = 'https://www.bestbuy.com/cart/json'
		h = self.headers
		h['X-ORDER-ID'] = self.cart_id
		r = self.s.get(url, headers=h)
		print(r)
		print(r.json())

	# def patch_billing():
	# 	url = 'https://www.bestbuy.com/checkout/standardizeAddress'
	# 	h = headers
	# 	h['X-Native-Checkout-Version'] = '__VERSION__'
	# 	h['X-User-Interface'] = 'DotCom-Optimized'
	# 	payload = {
	# 		'city': 'Atlanta',
	# 		'country': 'US',
	# 		'dayPhoneNumber': '4709914999',
	# 		'firstName': 'James',
	# 		'isWishListAddress': 'false',
	# 		'lastName': 'Han',
	# 		'middleInitial': '',
	# 		'override': 'false',
	# 		'saveToProfile': 'false',
	# 		'state': 'GA',
	# 		'street': '2850 Arrow Creek Dr',
	# 		'street2': '',
	# 		'userAddressAsBilling': 'false',
	# 		'zipcode': '30341'
	# 	}
	# 	r = s.post(url, headers=h, json=payload)
	# 	print(r)

	# def validate(self):
	# 	print('Validating checkout')
	# 	url = f'https://www.bestbuy.com/checkout/orders/{self.cart_id}/validate'
	# 	h = self.headers
	# 	h['X-User-Interface'] = 'DotCom-Optimized'
	# 	r = self.s.post(url, headers=h)
	# 	print(r)
	# 	print(r.url)
	# 	data = r.json()
	# 	print(data)

bb = BestBuyCA()
bb.add_to_cart()
bb.sign_in_as_guest()
bb.get_key()
bb.post_shipping()
bb.put_payment()
# bb.post_redirect()
# bb.get_cart()
# bb.checkout()
# bb.patch_item_info()
# bb.patch_guest_info()
# bb.get_key()
# bb.patch_payment()
# # bb.prelookup()
# bb.submit_payment()
# bb.verify_payment()