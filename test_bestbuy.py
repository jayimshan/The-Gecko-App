import requests
import json

import gecko_utils

class BestBuy:

	def __init__(self):

		self.s = requests.Session()

		self.headers = {
			'accept': 'application/json',
			'content-type': 'application/json; charset=UTF-8',
			'host': 'www.bestbuy.com',
			'origin': 'https://www.bestbuy.com',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'
		}

		# self.sku = 6257148
		self.sku = 5723319
		self.cart_id = None
		self.line_id = None
		self.token = None
		self.redirect_url = None
		self.order_id = None
		self.threeDS = None
		self.public_key = None
		self.key_id = None
		self.fulfillment_type = None

#--------------------CONFIRMED--------------------

	def add_to_cart(self):
		print('Adding to cart')
		url = 'https://www.bestbuy.com/cart/api/v1/addToCart'
		payload = {
			'items': [{
				'skuId': self.sku
			}]
		}
		h = self.headers
		h['X-CLIENT-ID'] = 'browse'
		h['X-REQUEST-ID'] = 'global-header-cart-count'
		r = self.s.get('https://www.bestbuy.com/basket/v1/basketCount', headers=h)
		for cookie in self.s.cookies:
			print(cookie)
		r = self.s.post(url, headers=self.headers, json=payload)

		print(self.s.cookies)
		print(r)
		print(r.url)
		data = r.json()
		self.line_id = data['summaryItems'][0]['lineId']
		print(data)

	def get_basket(self):
		print('Getting basket')
		# Get cart id
		url = 'https://www.bestbuy.com/basket/v1/basket'
		h = self.headers
		h['X-CLIENT-ID'] = 'not null'
		r = self.s.get(url, headers=h)
		print(r)
		data = r.json()
		print(data)
		self.cart_id = data['id']

	def select_shipping(self):
		url = f'https://www.bestbuy.com/cart/item/{self.line_id}/fulfillment'
		h = self.headers
		h['X-ORDER-ID'] = self.cart_id
		payload = {
			'selected': 'SHIPPING'
		}
		r = self.s.put(url, headers=h, json=payload)
		print(r)
		data = r.json()
		print(data)
		self.fulfillment_type = data['order']['lineItems'][0]['item']['fulfillmentType']

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

	def sign_in_as_guest(self):
		print('Signing in as guest')
		url = 'https://www.bestbuy.com/identity/guest'
		params = {
			'token': self.token
		}
		r = self.s.get(url, headers=self.headers, params=params)
		print(r)
		print(r.url)

	def patch_item_info(self):
		print('Patching item info')
		url = f'https://www.bestbuy.com/checkout/orders/{self.cart_id}/'
		h = self.headers
		h['X-User-Interface'] = 'DotCom-Optimized'
		payload = {
			'items': [{
				'id': self.line_id,
				'giftMessageSelected': False,
				'type': 'DEFAULT',
				'selectedFulfillment': {
					'shipping': {
						'address': {
							'city': 'Atlanta',
							'country': 'US',
							'dayPhoneNumber': '4709914999',
							'firstName': 'James',
							'isWishListAddress': False,
							'lastName': 'Han',
							'middleInitial': '',
							'override': False,
							'saveToProfile': False,
							'state': 'GA',
							'street': '2850 Arrow Creek Dr',
							'street2': '',
							'type': 'RESIDENTIAL',
							'useAddressAsBilling': False,
							'zipcode': '30341'
						}
					}
				}
			}]
		}
		r = self.s.patch(url, headers=h, json=payload)
		print(r)
		print(r.url)
		data = r.json()
		print(data)

	def patch_guest_info(self):
		print('Patching guest info')
		url = f'https://www.bestbuy.com/checkout/orders/{self.cart_id}/'
		h = self.headers
		h['X-User-Interface'] = 'DotCom-Optimized'
		payload = {
			'emailAddress': 'semajhan@gmail.com',
			'phoneNumber': '7737081444',
			'smsNotifyNumber': '',
			'smsOptIn': False
		}
		r = self.s.patch(url, headers=h, json=payload)
		print(r)
		print(r.url)
		data = r.json()
		print(data)
		self.order_id = data['customerOrderId']

	def get_key(self):
		url = 'https://www.bestbuy.com/api/csiservice/v2/key/tas'
		r = self.s.get(url, headers=self.headers)
		print(r)
		data = r.json()
		print(data)
		self.public_key = data['publicKey']
		self.key_id = data['keyId']

	def patch_payment(self):
		print('Patching payment')
		number = gecko_utils.get_encrypted_card(self.public_key, self.key_id, '4833130037628039')
		print(type(number))
		url = f'https://www.bestbuy.com/checkout/orders/{self.cart_id}/paymentMethods'
		h = self.headers
		h['X-User-Interface'] = 'DotCom-Optimized'
		payload = {
			'billingAddress': {
				'city': 'ATLANTA',
				'country': 'US',
				'dayPhoneNumber': '4709914999',
				'firstName': 'James',
				'isWishListAddress': False,
				'lastName': 'Han',
				'middleInitial': '',
				'override': False,
				'saveToProfile': False,
				'state': 'GA',
				'street': '2850 ARROW CREEK DR',
				'street2': '',
				'useAddressAsBilling': True,
				'zipcode': '30341'
			},
			'creditCard': {
				'binNumber': '483313',
				'cardType': 'VISA',
				'cid': '530',
				'expiration': {
					'month': '09',
					'year': '2020'
				},
				'govPurchaseCard': False,
				'hasCID': True,
				'invalidCard': False,
				'isCustomerCard': False,
				'isInternationalCard': False,
				'isNewCard': True,
				'isPWPRegistered': False,
				'isVisaCheckout': False,
				'number': number
			}
		}
		r = self.s.patch(url, headers=h, json=payload)
		print(r)
		data = r.json()
		print(data)

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
		url = 'https://www.bestbuy.com/checkout/api/1.0/paysecure/submitCardAuthentication'
		h = self.headers
		h['X-Native-Checkout-Version'] = '__VERSION__'
		h['X-User-Interface'] = 'DotCom-Optimized'
		payload = {
			'orderId': self.order_id,
			'threeDSecureStatus': {
				'threeDSReferenceId': self.threeDS
			}
		}
		r = self.s.post(url, headers=h, json=payload)
		print(r)

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

bb = BestBuy()
bb.add_to_cart()
# bb.get_cart()
# bb.checkout()
# bb.sign_in_as_guest()
# bb.patch_item_info()
# bb.patch_guest_info()
# bb.get_key()
# bb.patch_payment()
# # bb.prelookup()
# bb.submit_payment()
# bb.verify_payment()