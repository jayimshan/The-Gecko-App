from bs4 import BeautifulSoup
import requests
import json
# # # import re
# # # # import sys

# with open('store_colourpop_test/start_checkout.html', 'r', encoding='utf-8') as f:
# 	html = f.read()

# soup = BeautifulSoup(html, 'html.parser')
# # print(soup.prettify())
# # gateway = soup.find('input', {'id': })
# forms = soup.find_all('form')
# print(len(forms))
# # print(forms)
# inputs = forms[0].findChildren('input')
# for i in inputs:
# 	if 'honey' not in str(i):
# 		print('[VALUES]: {}'.format(i['name']))
# 	else:
# 		print('[HONEYPOT]: {}'.format(i['name']))
# token = soup.find_all('input', {'name': 'authenticity_token'})
# for t in token:
# 	print(t['value'])

# # pattern = re.compile('g-recaptcha-nojs')
# div = soup.find('div', {'class': 'g-recaptcha-nojss'})
# print('[DIV]: {}'.format(div))
# if div:
# 	print('[SITEKEY]: {}'.format(div.iframe['src'].split('=')[-1]))
# captcha = soup.find('textarea', id='g-recaptcha-response')
# print('[CAPTCHA]: {}'.format(captcha))

# print(sys.version)

# endpoint_sandbox = 'https://sandbox-rest.avatax.com/api/v2/taxrates/bypostalcode'
# endpoint_production = 'https://rest.avatax.com/api/v2/taxrates/bypostalcode'
# headers = {
# 	'Authorization': 'Basic MjAwMDE3MDQzNDo0MDkxNTA0Q0FERUE4RDc2',
# 	'Accept': 'application/json',
# 	'Method': 'GET'
# }
# params = {
# 	'country': 'United States',
# 	'postalCode': 30341
# }

# r = requests.get(endpoint_production, headers=headers, params=params).json()
# print(r)
# # data = r.json()
# # print(type(data['totalRate']))

# price = 17.95
# tax_rate = r['totalRate']
# tax = round(price * tax_rate, 2)
# total = price + tax
# print(tax)
# print(total)

# import urllib.parse

# code = urllib.parse.quote('{}-{}-{}'.format('shopify', '$0-$10', 6.95), safe='()$')
# print(code)

# url = 'https://colourpop.com/api/2020-01/checkouts.json'

# headers = {
# 	# 'authorization': 'Basic MWNiZGY3NjJlZGEyZWYwYWRjMTc0Y2IxYmQyMzU4NGY=',
# 	'host': 'colourpop.com',
# 	'x-shopify-storefront-access-token': '1cbdf762eda2ef0adc174cb1bd23584f',
# 	# 'method': 'POST',
# 	# 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
# 	# 'accept-encoding': 'gzip, deflate, br',
# 	# 'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7,pt;q=0.6',
# 	'content-type': 'application/json',
# 	# 'upgrade-insecure-requests': '1',
# 	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
# 	# 'x-requested-with': 'XMLHttpRequest'
# }

# # payload = json.dumps(
# # 	{
# # 		'checkout': {
# # 			'email': 'jamielee11022@gmail.com',
# # 			'line_items': [{
# # 					'variant_id': 32054687236178,
# # 					'quantity': 1
# # 				}],
# # 			'shipping_address': {
# # 				'first_name': 'Jamie',
# # 				'last_name': 'Lee',
# # 				'address1': '200 S Tennessee St',
# # 				'address2': None,
# # 				'company': None,
# # 				'city': 'Cartersville',
# # 				'country': 'US',
# # 				'province': 'GA',
# # 				'phone': '773-708-1444',
# # 				'zip': '30120',
# # 				'province_code': None,
# # 				'country_code': None,
# # 			}
# # 		}
# # 	}
# # )

proxy = {
	'https': 'https://kzaqzd:oefnla@63.115.149.158:17102'
}

# # r = requests.post(url, headers=headers, data=payload, proxies=proxy).json()
# # print(r)
# # token = r['checkout']['token']
# # print('\n[TOKEN]: {}'.format(token))
# token = '7759338542b94a6d827badd9ec5849f4'
# # token = '51f5640c6aaec2b0718694f9741bd6cf'
# # token = '444679abf097bc5e5d3e2adbed4f0494'
# # url = 'https://colourpop.com/api/2020-01/checkouts/{}/shipping_rates.json'.format(token)
# # print(url)
# # r = requests.get(url, headers=headers, proxies=proxy)
# # print(r.json())
# # print(r.headers)
# # print(r)
# # handle = r['shipping_rates'][0]['id']
# # print('\n[HANDLE]: {}'.format(handle))

# # payload = {
# # 	'checkout': {
# # 		'shopify_payments_account_id': 94425479
# # 	}
# # }

# # payload = json.dumps(
# # 	{
# # 		'checkout': {
# # 			'token': token,
# # 			'shipping_line': {
# # 				'handle': handle
# # 			}
# # 		}
# # 	}
# # )
# #------------------------------------------------------------------------
s = requests.Session()

# url = f'https://colourpop.com/api/2020-01/checkouts/{token}.json'
# # r = s.put(url, headers=headers, data=json.dumps(payload), proxies=proxy)
# r = s.get(url, headers=headers, proxies=proxy)
# # print(r.headers)
# data = r.json()
# print(data)
# payment_due = data['checkout']['payment_due']
# print(payment_due)

# # x_request_id = r.headers['x-request-id']
# # print(x_request_id)
# #------------------------------------------------------------------------
# # # payload = json.dumps(
# # # 	{
# # # 		'checkout': {
# # # 			'token': token,
# # # 			'billing_address': {
# # # 				'first_name': 'Jamie',
# # # 				'last_name': 'Lee',
# # # 				'address1': '200 S Tennessee St',
# # # 				'address2': None,
# # # 				'company': None,
# # # 				'city': 'Cartersville',
# # # 				'country': 'US',
# # # 				'province': 'GA',
# # # 				'phone': '773-708-1444',
# # # 				'zip': '30120',
# # # 				'province_code': None,
# # # 				'country_code': None,
# # # 			}
# # # 		}
# # # 	}
# # # )
# # # r = requests.put(url, headers=headers, data=payload, proxies=proxy).json()
# # # print(r)

# # # url = 'https://colourpop.com/api/2020-01/checkouts/{}/complete.json'.format(token)
# # # r = requests.post(url, headers=headers, proxies=proxy)
# # # print(r.status_code)
# # # print(r.json())

# session_headers = {
# 	'accept': 'application/json',
# 	'accept-encoding': 'gzip, deflate, br',
# 	'accept-language': 'en-US,en;q=0.5',
# 	'content-type': 'application/json',
# 	'host': 'deposit.us.shopifycs.com',
# 	'origin': 'https://checkout.us.shopifycs.com',
# 	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'
# }

# url = 'https://elb.deposit.shopifycs.com/sessions'
# payload = {
# 	'payment': {
# 		'credit_card': {
# 			'number': '4767 7182 2328 6180',
# 			'name': 'Jimmy Love',
# 			'month': '4',
# 			'year': '2025',
# 			'verification_value': '572'
# 		}
# 	}
# }

# print(json.dumps(payload))
# r = s.post(url, headers=session_headers, data=json.dumps(payload), proxies=proxy)
# print(r.status_code)
# # print(r.headers)
# session_id = r.json()['id']
# print(session_id)

# payload = {
# 	'payment': {
# 		'request_details': {
# 			'ip_address': '63.115.149.158',
# 			'accept_language': 'en-US,en;q=0.8,fr;q=0.6',
# 			'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
# 		},
# 		'amount': '16.04',
# 		'session_id': session_id,
# 		'unique_token': '13c43c53c4594661b5ee16fc20f0b28e'
# 	}
# }

# print(json.dumps(payload))
# url = f'https://colourpop.com/api/2020-01/checkouts/{token}/payments.json'
# r = s.post(url, headers=headers, data=json.dumps(payload), proxies=proxy)
# print(r.status_code)
# print(r.json())

# headers = {
# 	'authority': 'shop.funko.com',
# 	'method': 'GET',
# 	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
# 	'accept-encoding': 'gzip, deflate, br',
# 	'accept-language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7,pt;q=0.6',
# 	'origin': 'https://shop.funko.com',
# 	'referer': 'https://shop.funko.com/',
# 	'upgrade-insecure-requests': '1',
# 	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
# 	'x-requested-with': 'XMLHttpRequest'
# }

# url = 'http://finalstraw.com'
# headers = {
# 	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
# }
# try:
# 	r = requests.get(url, headers=headers)
# 	print(r.url)
# 	print(r.headers)
# except requests.ConnectionError:
# 	print('Connection error')
# print(r)
# soup = BeautifulSoup(r.text, 'html.parser')
# with open('test_colourpop.html', mode='w', encoding='utf-8') as f:
# 	f.write(soup.prettify())
# print(r.text)
# soup = BeautifulSoup(r.text, 'html.parser')
# with open('test_colourpop.html', mode='r', encoding='utf-8') as f:
# 	html = f.read()

# soup = BeautifulSoup(html, 'html.parser')
# # print(soup.prettify())
# element = soup.find('meta', {'name': 'shopify-checkout-api-token'})
# if element:
# 	token = element['content']
# 	print(token)
# 	data = json.loads(element.get_text())
# 	print(data['accessToken'])
# data = json.loads(token)
# print(data['accessToken'])

# import uuid
# i = uuid.uuid1()
# print(i)
# print(i.hex)


s = requests.Session()

print('Opening www.target.com')
url = 'https://www.target.com'
headers = {
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}
r = s.get(url, headers=headers, proxies=proxy)
c = r.cookies.get_dict()
tealeaf_id = c['TealeafAkaSid']
visitor_id = c['visitorId']
print(f'[TEALEAF ID]: {tealeaf_id}')
print(f'[VISITOR ID]: {visitor_id}')
# for c in r.cookies:
# 	print(c.name, c.value)

# ----------LOGIN----------
print('Logging in')
headers = {
	'accept': 'application/json',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'en-US',
	'content-type': 'application/json',
	'host': 'gsp.target.com',
	'origin': 'https://login.target.com',
	'referer': 'https://login.target.com/gsp/static/v1/login/?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_defualt=false&actions=create_session_signin',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
	'X-GyJwza5Z-a': 'X7XoZFWBcjYyTZ9aA2TAwiD6L3=EfY5wijX=bARjAMibrSRL-CMMl_ofAV3Ua_3Q5V6=y6oe1Aw1juOsTX2B=i8mrRBA-n1SpdN-WsKW=S3KsQfbe5rUpqnOrpQk0PmoPk-Zc6aFHB4eWStf4s=zuyvbw-7sVnalKgIatazJWekMCt=6ogk0eQ67sdQkJu8Waab9LukiKHjhrrrKFo9BvpPhx1DSdleWNbFTCqP=81o5EmKf8j7HtFujKVRm5LNeaKzM79ps_lz6uW9SXtaLKkOWctXPZuMoHxXIVn5T2lVsOd-dCdnDe2p4276MmhfeXMp-kasMespTjBL6WOd7CsNlzNEdvqdqFj8ZSCFe3Yz_P2c0D86k=95Nlo6f_nvfTcVExOBFSINj3gorjd91WUY2ZAwoARultbwVS=qzlTLnPcDFTFz6ZOR7u0TAQXcaZoAFBxsn2=PL17-ldUTInq9gKK1Cwc-eo1kx-zt9eIS=yk3OhkaS4Ya9ag1wfteKB_cJ1BrnewJfSFTYrczZAZppqkYR0unhh1Xw=xrcbDzYmq4v4RSb=Cph4NP2xVYWe6QjlBFToJwSTPwnAgQDuqRgvESr0vH1zn45O=ixQk3=Ej6Ba9yT7IkjVetDWJgxliaFImnQ=t=6bLWzA8HNZoaINctd9=hiRSCdggkQAyp6cFzI=5p-kBBv1vIHXYxdZKlo_ubM-gBn6R8NJ=s0OLFNYr_ZWrydNzgrT2gJ7ukzsqN8Fhre1XLkxZ7-kcU74EOakvdNISRXM0MM5tJ9DBCCwRWp2nb7_llJ2sKM8Iw7oErBA_sJA0S0e87Eq589hO-LvEFOP7Wg-DSU8EbkC2Mt4IkpQNm3JigzAXUMyt=PxP_z2q=QU6uSJvTMm3CfJU1qCYniZ12egMm6hD7u_MnJoPu5lNVvr5wozt13DYSsSnbNjRVaxIydy6USOV79WLv9Wt-ejOdX6RHe4_jd0d_u_VO6ffLe9fH9jOhEY9zu8ryIL1XRS2oTIYPX7NpLW=Bm=Ck_f_RjeWngXScnwY8BUTqkdAXTCBfKzBU1YEf-NIgSu=CUtw9kO5i9gTni6ljC3_ISWYWUf6OtnzRuBmBqnjj-FXYmNCTn0csj3LwXfZLQgPBQxZmn98slrSlv8RA6OKJD2q4g4-ObUpyiKCy8jmhyOfCIdwFD9iy3t43j6UZxMfYMTovMunHZR-oEL-PET5T=ZoCuLTpkZCuf-c2g2mChT_KHMkNL03d=LBarbLFsZO=f7oIffkxsVLeFw_XJyn2cckpCVNH0JM9fgnMidujLy1rr=gqr1MsNVZIvkpgRupi_gzMYO5ISNyZ433yvoYdWCV90mq45E7FXT30kHpgvasC3r0sHcLFxhOIwp-rZ5LfPxF7nXdjFx18lvZa8IzanlYRv2vqqr0QUA3ZgZWdAe3kSMVZ--2JuQpUkJj88SBSaSZItNUL295dICb2ogwaanUuLqmMvefh3k_Un1RsZqnz1miR6fW3bO0dDDTYj9dO6fvmD9cdPuBSnIne_1e0jdgHS1Uznnd68jWiU1QNql1Wcm1CN0vrCXh1DwScp-xzylemAD6mhkh8KCvpJYWKDjma5hQZie0CfbklUcwTqJMDALLDu1jq39p=q8IBVXM4nRSxTVeZKkmEsdenp-bpfbLOTJC7ONdyHYkH4aaq14MCaCTwUWgXTWLg98e-CwcgY265ifJY-3sqwzjA9N9Qick=0ug4kxsHqa6h0Ho2N2Km-v86_iNSv3hBVaTgfDDWqLf1QOD1b-IDk62z1f3rtbDYmH=MlooenPB0aNKu-_x1=UJi6iEdlcSAy6dIgceOOviN89uDwA3peI=hjKOCgttYj61SYuw1mQJxewYvE7YfQeZCcQmRr618NsrsrHS1uaN09aLd0f4HzUkiepmWzNbiYlX-IQTBpt1eRpfuVDh-6Y6-CzmF2qHaVq=zH9=RSsboHFzl1efSc33n1nWUmCoXC5q=ib9mOPmVDtmuhOsdp1MQh-Fbb9OaPZdV9W2v=fEgwVxP1lQ6KWdUpl9QS91FjxMknIcIMljNjeTQSthRk2vZyDXyCcdbXdzJJV1LVlrRDyn5Koxx0ZBLxiP5YNsQaAhNRsIEjnRsJMPZWRo9MM60K4ZmvQsL8Ik90_edMw3rvhURMeff3KRusWbVXVILH8hrDm-34X=y0JKnPkSBJISRRDTIn3kHR11lhuXAjxVo0o52KDK=XENA7v2AOzHw6OStOYDaLa874-saNhT9x5wB_56XNK9CJtsTEw2F3jcO3zFFZq2mZ-7xBHwbYYfMOArOJ8qdnBsb-YPY1LVOQrckH7Alm-x5oMsg89ig3oSVcsH_EKMe=z0OOzP_nBfXY_TkID2eqZplsfPhM_AsVaMrYpi0v8PyTejaExImoLCaSapQ_V4SZNelv6prDCkE7U9ZJCbRIaR8e_bJuKR8uy85CwAKQSSIC0UWNuyTSCug6EJNPPHeiWygepv9cjZhizpL8tJYo9ssIpg9cxarrqaaJUasD3vsg2nbY7vyLdlFEnUpzspKfpkiFiWFEDgfJnvbFwoBRp_Qg5Q97bPu8efIhSLUQH0Jk-K35SEn9vEA2fSXeW9Q8d2gpQUCW3hxltJ2jZ8YFJAd_lp2LFaetMRzepil0Mrad=p9g9Y0CV6bm5AjzCcx-VKhzO9OHIqJbibjiQlVz6rW-vOEdNXvCk11BlmCClZ6416tHTSX15Rx-9gJW5UMlKIKeNqY1wJ23M5ScIixS81M4xJKyAI5lZ04rX3yRRaSLXVis=2ytM0F5HsBYTSSz1L-31oqnKqqwMf7Pk_7_=bkb_63vHA=hzpFsB6Zs3T3slUxQ3=36Ww2bnNKYvjks3f8CY0VZ0U7sHOIAY6Xrg9vmmM2ldbZKpE0EMwrR-3IWKbN3JuEJNcUwlgMpyQMdF=vJHC0oQBBURSZ6g8RQkRDVJuhE=-H8iK_Lmv4tpdhWhYQqbio_HTBeBrT_kddKFSgCaia2kQN9fca8Y7SWc0y=gFhbzO9S-h0YgWFBpzlvUPfhh=k1PFdEEPNpi2Y1RYuYbZAQnvELrcJDSPWz_lHz37PxhBiElIWNj4QHi_JDllLizd3xg06QNMB_5ZKqPCqDq5=_eepoVuPxA7R3sp06n9=dFwPlgRpENz-nMo4tJsS_fXJ4kRmcSuossO=bbfMV=fxw07ld6gOaKQyEBs8F5CxAl8XzWExwXQiRasdxBEudIQThKJHfoAveIsaLS2_QjOngOLt8gHHFmz0miA9dxKxBHQ4Zv73FTYwEjvozTsHmTfaTFxrUJs-EfNaj6=E_m-5SSCZlUgi1cW-gST8UAUeUwvwJwwJwJ_5oCrv1VlJELu9gOfa4J6MQbvW55K1X7-K-EaIeIZAFM=bLdlhFDoM_iOcaETBY6MTgcRkxNAdr5klXy3jMXKkwyRB6T4wDTUeMfhgu8OTHFrSeJoQTUdrBKWkVbiqSVfUgE4VF1u6ut3d3fFM9hRzmVRJjKg5YxmLZTv4DFMfBbY8=Zt2JyNWLN0yE_0sL5c_WMgx2mu1xKuBHQwsTOm=Wb2EqVJ4aubxrVU3=A_xdzdTmx77K1IiF7NJ991cOYdpR2AUmEM0-mSoQqs66Pp9wLm-KXL=CN7gYBWmLy8UnX0BTDCCzkvYEkI9rS1MxDp4qXrgb6ofF4O378R7qmUZBXys41X4g9Xlp1p-TP8oEAkAKoJje1TuqnrQ-Sj_lOzJevS_zh7YAS0W6bDdFvOqn5bQ8MYY0mg=K3ID_N8_hmH_H1aC5Bc1ll_MIDY1vvEwhts7ArzA8lj=SAdIHI8C4zjTe47RZBCfDDLWMkXpdAOCBLjcTRsQJI2gNBHmUAiFJrjB=VeMg5F_YTJEHlhB2zVTS-gtnKAVK5Nj4Wn2JLeF6Zwlda2hzh81_tMrJkQnFfjIJu_cgZcjc_fs9O8RPL5Bwz5LABSQu3LH7BoNXQ=SD_wo=YaIRhPxIFofFWNdaM2emmnXMwLDihBtp6WnQwLLhUoUwnJPM7Lk2EVreEle=MHB7D4Vf8YcWzZgWDLRBtagPjz6DH7yQkkJj9ZkNHhQVILIM-ZIylZdctI6QTbRK-9LcjkcsotUXFNRDnKh79A6luHFOXDhaF-fv=760eKDHlyMAsRiQPm3VwHWo7zOgkmUsR75gumh6DaBfqrBji=dLl_5l=RUFEej9xY-qhBDgb3-sQx84yUSIgk=nyTAHZ9mK_gUn3j2pHkUBONxHbt_QHpBQfI5kZxZoY3KxxadPqTNRqLZlzb0uZrzVm7HBMW0bzWTmnAoHc-1Iwq3BkHRTBreMP-JbmTqsZUt_NSO2JAQH9PqH3lhQfawzsgjDIi7p57IpywqAmwBTv8YuRTPhRu9mH8HYlQfxpl-o1RH=wUlIWZiiszu=35YJR8yaeDugJTn5Op6z=oUI_sPXYssInC-JOj1ENfjKZpgLgOrCv=ZcPUB2pW6UKiTuL2qhn3qJLrMpDevIcZW0Q8sq6WFspC1MkckovPi_WOmRNMSmPfxbnwFCTBwmLXcsQcf-tHxirWEIN=2wl8t4=ZHdOuXL0WYYb9U7onklA7jDZF5Hgo-=YPY4AZwXY5IOgdfItq0JAMEsv2bz0dr2TQyOpg3kVRMv5HD5b6Qh8Lyz--Uvls=8x2tMqARvZDu82MMTxrXb6w=KP8vzV2tPHTIa00ZILZIfJMAyV1XAuqJE3hxy2MvNLSYxX0TJTPJkkoNEpF05WVjCAu5S_Navh89nJ0_76bszyk6ASFV6D1ctSrrWQAdp1vRecvu5MiV4P_ycE2wBrbzxIUVPdh0YVgQ7LiS5l6cj9pxxMjUu2Bj0mAXvhWi3plO_HcVm=UOlwXj2TvelKKtsz7OzLRI-XKBXgRzPnLup=2xdlo=S5jFw-mFFVm5XN9qsMSF2jH6DpkzD3OoZo=dyt8P4hu0C23dDyjDUYlRETBX5C8b8L5oEEodnRajx0BV_FX4FNuDc2=2c',
	'X-GyJwza5Z-b': 'hjomdr',
	'X-GyJwza5Z-c': 'AABPAh5xAQAAAJvzmLOYcdgtJok5f9KTviHeHLNXfzDGeSXSE8AmSjWVA_Ij',
	'X-GyJwza5Z-d': 'o_0',
	'X-GyJwza5Z-f': 'A3nXEh5xAQAAOnteIvZDeXHTxjRgiybsI3iGtf4UaDUJW4PpLlrS2Bn7LH1YAUlq1AucuMmZwH8AAEB3AAAAAA==',
	'X-GyJwza5Z-z': 'p',
	'x-username': 'jayimshan@gmail.com'
}
payload = {
	'username': 'jayimshan@gmail.com',
	'password': 'Miho6446',
	'keepMeSignedInChecked': False
}
url = 'https://gsp.target.com/gsp/authentications/v1/credential_validations?client_id=ecom-web-1.0.0'
r = s.post(url, headers=headers, json=payload, proxies=proxy)
print(r)
print(r.json())

# ----------TOKENS----------
print('Getting access token')
url = 'https://gsp.target.com/gsp/oauth_tokens/v2/client_tokens'
headers = {
	'accept': '*/*',
	'accept-encoding': 'gzip, deflate, br',
	'content-type': 'application/json',
	'host': 'gsp.target.com',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}
payload = {
	'grant_type': 'refresh_token',
	'client_credential': {
		'client_id': 'ecom-web-1.0.0'
	},
	'device_info': {
		'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
		'language': 'en-US',
		'color_depth': '24',
		'device_memory': '8',
		'pixel_ratio': 'unknown',
		'hardware_concurrency': '8',
		'resolution': '[1920,1080]',
		'available_resolution': '[1920,1080]',
		'timezone_offset': '240',
		'session_storage': '1',
		'local_storage': '1',
		'indexed_db': '1',
		'add_behavior': 'unknown',
		'open_database': '1',
		'cpu_class': 'unknown',
		'navigator_platform': 'Win32',
		'do_not_track': 'unknown',
		'adblock': 'false',
		# 'visitor_id': visitor_id,
		# 'tealeaf_id': tealeaf_id,
		'os_name': 'Windows',
		'os_version': '10'
	}
}
# payload = {
# 	'grant_type': 'authorization_code',
# 	'client_credential': {
# 		'client_id': 'ecom-web-1.0.0'
# 	},
# 	'code': '',
# 	'device_info': {
# 		'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
# 		'language': 'en-US',
# 		'color_depth': '24',
# 		'device_memory': '8',
# 		'pixel_ratio': 'unknown',
# 		'hardware_concurrency': '8',
# 		'resolution': '[1920,1080]',
# 		'available_resolution': '[1920,1080]',
# 		'timezone_offset': '240',
# 		'session_storage': '1',
# 		'local_storage': '1',
# 		'indexed_db': '1',
# 		'add_behavior': 'unknown',
# 		'open_database': '1',
# 		'cpu_class': 'unknown',
# 		'navigator_platform': 'Win32',
# 		'do_not_track': 'unknown',
# 		'adblock': 'false',
# 		# 'visitor_id': visitor_id,
# 		# 'tealeaf_id': tealeaf_id,
# 		'os_name': 'Windows',
# 		'os_version': '10'
# 	}
# }
r = s.post(url, headers=headers, json=payload, proxies=proxy)
print(r)
print(r.json())

# ----------VALIDATE TOKENS----------
print('Validating tokens')
url = 'https://gsp.target.com/gsp/oauth_validations/v3/token_validations'
headers = {
	'content-type': 'application/json',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}
payload = {}
r = s.post(url, headers=headers, json=payload)
print(r)
print(r.json())

# ----------GET CART----------
print('Getting cart')
url = 'https://carts.target.com/web_checkouts/v1/cart'
# url = 'https://www.target.com/co-cart'
headers['x-application-name'] = 'web'
params = {
	'field_groups': 'CART,CART_ITEMS,SUMMARY,PROMOTION_CODES,ADDRESSES',
	'key': 'feaf228eb2777fd3eee0fd5192ae7107d6224b39'
}
payload = {
	'cart_type': 'REGULAR',
	'channel_id': 10,
	'shopping_context': 'DIGITAL',
	# 'shopping_location_id': '1390',
	'guest_location': {
		'country': 'US',
		'state': 'GA',
		'zip': '30341'
	}
}
r = s.put(url, headers=headers, json=payload)
print(r)
# print(r.json())
print(r.text)

# ----------AUTH CODE----------
# Get login-session cookie
# print('Getting login session cookie')
# url = 'https://gsp.target.com/gsp/authentications/v1/auth_codes'
# headers = {
# 	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
# }
# params = {
# 	'client_id': 'ecom-web-1.0.0',
# 	'state': '1585234912413',
# 	'redirect_uri': 'https://www.target.com/',
# 	'assurance_level': 'M'
# }
# r = s.get(url, headers=headers, params=params, proxies=proxy)
# print(r)

# ----------CREATE SESSION SIGN IN----------
# print('Creating session id')
# url = 'https://login.target.com/gsp/static/v1/login/'
# headers = {
# 	'authority': 'login.target.com',
# 	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
# 	# 'content-type': 'multipart/form-data',
# 	'upgrade-insecure-requests': '1',
# 	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
# }
# payload = {
# 	'username': 'jayimshan@gmail.com',
# 	'password': 'Miho6446',
# 	'keepMeSignedIn': 'false'
# }
# params = {
# 	'client_id': 'ecom-web-1.0.0',
# 	'ui_namespace': 'ui-default',
# 	'back_button_action': 'browser',
# 	'keep_me_signed_in': 'true',
# 	'kmsi_defualt': 'false',
# 	'actions': 'create_session_signin'
# }
# r = s.post(url, headers=headers, json=payload, proxies=proxy)
# print(r)
# print(r.text)

# ----------SESSION VALIDATION----------
# print('Validating session')
# url = 'https://gsp.target.com/gsp/authentications/v1/session_validations'
# # url = 'https://login.target.com/'
# headers = {
# 	'accept': 'application/json',
# 	'accept-encoding': 'gzip, deflate, br',
# 	'content-type': 'application/json',
# 	'host': 'gsp.target.com',
# 	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
# }
# r = s.get(url, headers=headers, proxies=proxy)
# print(r)


# for c in s.cookies:
# 	print(f'[NAME]: {c.name} [VALUE]: {c.value}')

# ----------CART----------
# headers = {
# 	'authority': 'carts.target.com',
# 	'accept': 'application/json',
# 	'accept-encoding': 'gzip, deflate, br',
# 	'content-type': 'application/json',
# 	'origin': 'https://www.target.com',
# 	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
# 	'x-application-name': 'web'
# }

# url = 'https://carts.target.com/web_checkouts/v1/cart_items'

# payload = {
# 	'cart_type': 'REGULAR',
# 	'channel_id': '10',
# 	'shopping_context': 'DIGITAL',
# 	'cart_item': {
# 		'tcin': '52161284',
# 		'quantity': 1,
# 		'item_channel_id': '10'
# 	}
# }

# params = {
# 	'field_groups': 'CART,CART_ITEMS,SUMMARY',
# 	'key': 'feaf228eb2777fd3eee0fd5192ae7107d6224b39'
# }

# r = s.post(url, headers=headers, json=payload, proxies=proxy)
# print(r)
# print(r.json())