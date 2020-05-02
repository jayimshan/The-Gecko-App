import requests
import random
import queue
import time

import gecko_utils

proxy_list = [
	'63.115.150.219:17102:imjztp:npyscc',
	'63.115.148.26:17102:qjpabz:jijzad',
	'63.115.149.196:17102:iwqoma:vjqjjm',
	'63.115.148.214:17102:edtmqr:kmzorr',
	'63.115.148.129:17102:pwlvkq:niaupq',
	'63.115.151.50:17102:twrege:uqpwzj',
	'63.115.151.52:17102:qbrkwo:yuqdrg',
	'63.115.149.25:17102:fdchhf:kzqetd',
	'63.115.148.238:17102:gagpff:lykwqi',
	'63.115.148.234:17102:lpufvc:vfnyyc',
	'63.115.150.56:17102:oqxrjt:eoltxk',
	'63.115.150.222:17102:tgdxnb:awgojn',
	'63.115.151.21:17102:fcghlr:hsrwim',
	'63.115.148.180:17102:ygauey:cejeht',
	'63.115.149.18:17102:pjhfmu:ujkbzq',
	'63.115.148.15:17102:keodmu:chdapl',
	'63.115.150.199:17102:lzanwf:noryyp',
	'63.115.151.89:17102:kroynm:eezztt',
	'63.115.151.32:17102:dlubgw:gkbjbp',
	'63.115.150.126:17102:lmfwez:wocpfw',
	'63.115.148.17:17102:hmyshp:wujfku',
	'63.115.149.158:17102:kzaqzd:oefnla',
	'63.115.149.155:17102:mwbqqu:dgplop',
	'63.115.149.143:17102:ikpqrp:ajvwnw',
	'63.115.151.3:17102:eyilbq:ghbkxl'
]

q = queue.Queue()

for proxy in proxy_list:
	parts = proxy.split(':')
	combined = {'https': 'https://{}:{}@{}:{}'.format(parts[2], parts[3], parts[0], parts[1])}
	q.put(combined)

p = None

def get_proxy(proxy):
	if proxy is None:
		return q.get()
	else:
		q.put(proxy)
		return q.get()
# print(p)

def delay_range():
	return round(random.uniform(2, 4), 2)

tcin = 77464002

url = f'https://redsky.target.com/v3/pdp/tcin/{tcin}'
headers = {
	'accept': 'application/json',
	'content-type': 'application/json',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}
params = {
	'excludes': 'taxonomy,bulk_ship,awesome_shop,question_answer_statistics,rating_and_review_reviews,rating_and_review_statistics,deep_red_labels,in_store_location',
	'key': 'eb2551e4accc14f38cc42d32fbc2b2ea'
}

run_once = True
previous_stock = 0

# while run_once:
# 	p = get_proxy(proxy=p)
# 	print(f'Trying with proxy: {p}')
# 	r = requests.get(url, headers=headers, params=params, proxies=p)
# 	data = r.json()
# 	stock = int(data['product']['available_to_promise_network']['available_to_promise_quantity'])
# 	status = data['product']['available_to_promise_network']['availability_status']
# 	if stock > previous_stock or 'out' not in status.lower():
# 		previous_stock = stock
# 		try:
# 			title = data['product']['item']['product_description']['title']
# 			store = 'https://www.target.com/'
# 			link = data['product']['item']['buy_url']
# 			image_url = data['product']['item']['enrichment']['images'][0]
# 			src = f'{image_url["base_url"]}{image_url["primary"]}'
# 			url = 'https://discordapp.com/api/webhooks/694756356519100536/-X5G9HyW0sx5Wc6-Pza9SOKKbrzMJmarwieqVIREWgT-i7vHd6bJTeJFnAaY-okVoTfm'
# 			gecko_utils.post_monitor_custom_webhook(url, title, store, link, src, status, stock)
# 		except Exception as e:
# 			print(f'{e}')
# 	print(f'[Stock]: {stock}')
# 	print(f'[Status]: {status}')
# 	delay = delay_range()
# 	print(f'Retrying in: {delay}')
# 	time.sleep(delay)
	# run_once = False