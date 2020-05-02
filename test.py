# --------------------URL Encode--------------------
# import urllib.parse

# style_id = 75352
# qty = 1
# sub = '{{"{}":{}}}'.format(style_id, qty)
# # sub = f''
# code = urllib.parse.quote('{}'.format(sub), safe='()')

# print(code)

# --------------------Monitor--------------------
# from discord_webhook import DiscordWebhook, DiscordEmbed
# from bs4 import BeautifulSoup

# import requests
# import random
# import queue
# import time

# s = requests.Session()
# url = 'https://chucksperry.net/widespread-panic-beacon-theatre-new-york-city-2020/'

# headers = {
# 	'authority': 'chucksperry.net',
# 	'method': 'GET',
# 	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
# 	# 'accept-encoding': 'gzip, deflate, br',
# 	'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7,pt;q=0.6',
# 	'content-type': 'text/html; charset=utf-8',
# 	'upgrade-insecure-requests': '1',
# 	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
# 	# 'x-requested-with': 'XMLHttpRequest'
# }

# proxy_list = [
# 	'63.115.150.219:17102:imjztp:npyscc',
# 	'63.115.148.26:17102:qjpabz:jijzad',
# 	'63.115.149.196:17102:iwqoma:vjqjjm',
# 	'63.115.148.214:17102:edtmqr:kmzorr',
# 	'63.115.148.129:17102:pwlvkq:niaupq',
# 	'63.115.151.50:17102:twrege:uqpwzj',
# 	'63.115.151.52:17102:qbrkwo:yuqdrg',
# 	'63.115.149.25:17102:fdchhf:kzqetd',
# 	'63.115.148.238:17102:gagpff:lykwqi',
# 	'63.115.148.234:17102:lpufvc:vfnyyc',
# 	'63.115.150.56:17102:oqxrjt:eoltxk',
# 	'63.115.150.222:17102:tgdxnb:awgojn',
# 	'63.115.151.21:17102:fcghlr:hsrwim',
# 	'63.115.148.180:17102:ygauey:cejeht',
# 	'63.115.149.18:17102:pjhfmu:ujkbzq',
# 	'63.115.148.15:17102:keodmu:chdapl',
# 	'63.115.150.199:17102:lzanwf:noryyp',
# 	'63.115.151.89:17102:kroynm:eezztt',
# 	'63.115.151.32:17102:dlubgw:gkbjbp',
# 	'63.115.150.126:17102:lmfwez:wocpfw',
# 	'63.115.148.17:17102:hmyshp:wujfku',
# 	'63.115.149.158:17102:kzaqzd:oefnla',
# 	'63.115.149.155:17102:mwbqqu:dgplop',
# 	'63.115.149.143:17102:ikpqrp:ajvwnw',
# 	'63.115.151.3:17102:eyilbq:ghbkxl'
# ]

# q = queue.Queue()

# for proxy in proxy_list:
# 	parts = proxy.split(':')
# 	combined = {'https': 'https://{}:{}@{}:{}'.format(parts[2], parts[3], parts[0], parts[1])}
# 	# print(combined)
# 	q.put(combined)

# p = None

# def get_proxy(proxy):
# 	if proxy is None:
# 		return q.get()
# 	else:
# 		q.put(proxy)
# 		return q.get()
# # print(p)

# def delay_range():
# 	return round(random.uniform(4, 8), 2)

# form_count = 2
# url_webhook = 'https://discordapp.com/api/webhooks/686131140964122650/xbHKoXbJSBaYaEEm2SkwwNJ2upEifkSZWWVt7VvTxXrNFl_QtGQkHn6QVhgCePaO8_fA'
# # url_webhook = 'https://discordapp.com/api/webhooks/601232887219748874/tu1D8PBWC7STcVZ0nPArrvKiFoSVApLroINAOHC54a9SUA0XKKrE-DVj5TKw3JEF4_-P'

# while True:
# 	p = get_proxy(proxy=p)
# 	print('Trying with proxy: {}'.format(p))
# 	r = s.get(url, headers=headers, proxies=p)
# 	soup = BeautifulSoup(r.text, 'html.parser')
# 	forms = soup.find_all('form')
# 	print('Forms: {}'.format(len(forms)))
# 	if form_count < len(forms):
# 		form_count = len(forms)
# 		try:
# 			webhook = DiscordWebhook(url_webhook)
# 			embed = DiscordEmbed(title='Widespread Panic', color=0x3cd13a)
# 			embed.set_author(name='Possible "Pay Now Button" detected')
# 			# embed.add_embed_field(name='Store', value='{}'.format(store))
# 			# embed.add_embed_field(name='Price', value='{}'.format(price))
# 			# embed.add_embed_field(name='Qty', value='{}'.format(qty))
# 			embed.add_embed_field(name='Link', value='https://chucksperry.net/widespread-panic-beacon-theatre-new-york-city-2020/')
# 			# embed.add_embed_field(name='Color', value='{}'.format(color))
# 			# embed.add_embed_field(name='Size', value='{}'.format(size))
# 			embed.set_thumbnail(url='https://chucksperry.net/wp-content/uploads/2020/02/PANIC-SPERRY-COLOR-WEB.jpg')
# 			embed.set_footer(text='Powered by The Gecko App | @jayimshan', icon_url='https://i.imgur.com/E6zcSEY.png')
# 			embed.set_timestamp()
# 			webhook.add_embed(embed)
# 			webhook.execute()
# 		except Exception as e:
# 			print(str(e))
# 	else:
# 		print('scanning')
# 	delay = delay_range()
# 	print('Sleeping for: {}'.format(delay))
# 	time.sleep(delay)


# --------------------Queue--------------------
# import queue

# q = queue.Queue()

# items = [0, 1, 2]
# for item in items:
# 	print('Putting into queue: {}'.format(item))
# 	q.put(item)

# for i in range(len(items) + 1):
# 	print('Getting from queue')
# 	try:
# 		num = q.get(timeout=5)
# 		print('Item: {}'.format(num))
# 	except queue.Empty:
# 		print('Queue is empty!')

# print('Done')

# import json

# payload = json.dumps({
# 	'items': [
# 		{
# 			'quantity': 2,
# 			'id': 794864229
# 		}
# 	]
# })

# print(payload)

# import os

# if not os.path.exists('myfolder'):
# 	os.makedirs('myfolder')

# with open('myfolder/name.txt', mode='w') as f:
# 	f.write('blablabla')

price = int(500 * 0.01)
print('${}.00'.format(price))