from bs4 import BeautifulSoup

import requests
import json
import datetime

# url = 'https://discordapp.com/api/webhooks/601232887219748874/tu1D8PBWC7STcVZ0nPArrvKiFoSVApLroINAOHC54a9SUA0XKKrE-DVj5TKw3JEF4_-P'
# time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
# print(time)
# payload = {
# 	'username': 'Success',
# 	'avatar_url': 'https://i.imgur.com/E6zcSEY.png',
# 	'embeds': [{
# 		'title': 'The Gecko App just cooked:',
# 		'description': '[Nintendo - Switch 32GB Console - Neon Red/Neon Blue Joy-Con](https://www.bestbuy.com/site/nintendo-switch-animal-crossing-new-horizons-edition-32gb-console-multi/6401728.p?skuId=6401728)',
# 		'color': 9946999,
# 		'thumbnail': {
# 			'url': 'https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6401/6401728_sd.jpg;maxHeight=640;maxWidth=550'
# 		},
# 		'fields': [
# 			{
# 				'name': 'Store',
# 				'value': 'asd',
# 				'inline': True
# 			},
# 			{
# 				'name': 'Price',
# 				'value': 'asd',
# 				'inline': True
# 			},
# 			{
# 				'name': 'Qty',
# 				'value': 'asd',
# 				'inline': True
# 			},
# 			{
# 				'name': 'Link',
# 				'value': '[asd](https://www.google.com)',
# 				'inline': True
# 			},
# 			{
# 				'name': 'Color',
# 				'value': 'asd',
# 				'inline': True
# 			},
# 			{
# 				'name': 'Size',
# 				'value': 'asd',
# 				'inline': True
# 			}
# 		],
# 		'footer': {
# 			'text': 'Powered by The Gecko App | @jayimshan',
# 			'icon_url': 'https://i.imgur.com/E6zcSEY.png'
# 		},
# 		'timestamp': time
# 	}]
# }

# r = requests.post(url, json=payload)
# print(r)
# url = 'https://www.target.com/'
# headers = {
# 	'accept': 'application/json',
# 	'content-type': 'application/json',
# 	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
# }
# r = requests.get(url, headers=headers, proxies=None)
# print(r)

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
params = {
	'client_id': 'ecom-web-1.0'
}

s = requests.Session()

url = 'https://gsp.target.com/gsp/authentications/v1/credential_validations'

r = s.post(url, headers=headers, json=payload)
print(r)
data = r.json()
print(data)