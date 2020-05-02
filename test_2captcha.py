import requests

api_key = 'ee5d7a0260ab239c83099cc055be5261'
url = 'https://www.shop.funko.com'
sitekey = '6LeoeSkTAAAAAA9rkZs5oS82l69OEYjKRZAiKdaF'
method = 'userrecaptcha'
captcha_id = None
post = 'http://2captcha.com/in.php?key={}&method={}&googlekey={}&pageurl={}&json=1'.format(api_key, method, sitekey, url)
get = 'https://2captcha.com/res.php?key={}&action=get&id={}&json=1'.format(api_key, captcha_id)
token = None

response = requests.get(post)
print(response.json())