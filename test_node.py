# from requests_html import HTMLSession
# import requests
# import urllib.parse
# import json

# session = HTMLSession()

# headers = {
# 	'authority': 'shop.funko.com',
# 	'method': 'GET',
# 	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
# 	'accept-encoding': 'gzip, deflate, br',
# 	'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7,pt;q=0.6',
# 	'content-type': 'application/x-www-form-urlencoded',
# 	'origin': 'https://shop.funko.com',
# 	'referer': 'https://shop.funko.com',
# 	'upgrade-insecure-requests': '1',
# 	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
# }

# r = session.get('https://shop.funko.com/10522158/checkouts/003a4a328bd62333776d35f4f3e177d2', headers=headers)
# r.html.render()
# print(r.html.html)

# headers = {
# 	'accept': 'application/json',
# 	'accept-encoding': 'gzip, deflate, br',
# 	'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7,pt;q=0.6',
# 	'content-type': 'application/json',
# 	'host': 'deposit.us.shopifycs.com',
# 	'origin': 'https://checkout.us.shopifycs.com',
# 	'upgrade-insecure-requests': '1',
# 	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
# }

# url = 'https://shop.funko.com/cart/shipping_rates.json?shipping_address[zip]=30066&shipping_address[country]=United States&shipping_address[province]=GA'
# r = requests.get(url, headers=headers).json()
# print(r)

# code = 'shopify-Flat Rate Shipping (we cannot ship to P.O. Boxes)-6.95'
# print(urllib.parse.quote(code, safe='()'))

# payload = {
# 	'credit_card': {
# 		'number': '1234 1234 1234 1234',
# 		'name': 'John Lee',
# 		'month': '9',
# 		'year': '2020',
# 		'verification_value': '530'
# 	}
# }

# payload = json.dumps(payload)
# print(type(payload))

# # endpoint = 'https://elb.deposit.shopifycs.com/sessions'
# endpoint = 'https://deposit.us.shopifycs.com/sessions'

# r = requests.post(endpoint, headers=headers, data=payload)
# print(r.status_code)
# print(r.text)

# endpoint = 'https://cdn.shopify.com/app/services/10522158/javascripts/checkout_countries/80679993410/en/countries-a1b1a5d840013c88df26870e5875ba8b61c78a9f-1580764708.js?version=2019-01-21'

board = [
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 0, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1]
]

def solve():
	for y in range(len(board)):
		for x in range(len(board)):
			if board[y][x] == 0:
				pass

def test():
	for i in range(5):
		print(i)
		for j in range(5):
			print(j)
			for k in range(5):
				print(k)
				return
	print('End')

test()