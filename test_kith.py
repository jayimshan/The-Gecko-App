from datetime import datetime

import requests
import json
import math

headers={
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "content-type": "application/json",
    "referer": "https://www.bestbuy.com/checkout/r/payment",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
}

sku_id = 6257142

url = 'https://www.bestbuy.com/checkout/r/fufillment'

payload = {
	'checkout': {
		'line_items': [{
			'variant_id': '19437156761728',
			'quantity': 1
		}],
	}
}

# url = 'https://www.bestbuy.com/api/tcfb/model.json'
# params = {
# 	'paths': json.dumps([
# 		["shop", "scds", "v2", "page", "tenants", "bbypres", "pages", "globalnavigationv5sv", "header"],
# 		["shop", "buttonstate", "v5", "item", "skus", f'{sku_id}', "conditions", "NONE", "destinationZipCode", "%20", "storeId", "%20", "context", "cyp", "addAll", "false"]
# 		]),
# 	'method': 'get'
# }
url = 'https://www.bestbuy.com/'
s = requests.Session()
r = s.get(url, headers=headers)
print(r)
cookie = None
for c in r.cookies:
	if 'abck' in c.name:
		print(c.value)
		cookie = c.value

url = 'https://www.bestbuy.com/resources/b564d4d214196368bcbb9625d68ac8'
# url = 'http://apid.cformanalytics.com/api/v1/_bm_/data'

sensor_data_1 = {
	'sensor_data': f'7a74G7m23Vrp0o5c9163791.54-1,2,-94,-100,Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0,uaend,11059,20100101,en-US,Gecko,0,0,0,0,390770,761395,5120,1410,5120,1440,1709,1330,3083,,cpen:0,i1:0,dm:0,cwen:0,non:1,opc:0,fc:1,sc:0,wrc:1,isc:105,vib:1,bat:0,x11:0,x12:1,5561,0.621120255310,794095380697.5,loc:-1,2,-94,-101,do_en,dm_en,t_dis-1,2,-94,-105,0,0,0,0,1487,231,0;0,-1,0,1,1627,1627,0;-1,2,-94,-102,0,0,0,0,1487,231,0;0,-1,0,1,1627,1627,0;-1,2,-94,-108,-1,2,-94,-110,-1,2,-94,-117,-1,2,-94,-111,-1,2,-94,-109,-1,2,-94,-114,-1,2,-94,-103,-1,2,-94,-112,https://www.bestbuy.com/-1,2,-94,-115,1,32,32,0,0,0,0,2,0,1588190761395,-999999,16990,0,0,2831,0,0,7,0,0,{cookie},31421,-1,-1,26067385-1,2,-94,-106,0,0-1,2,-94,-119,-1-1,2,-94,-122,0,0,0,0,1,0,0-1,2,-94,-123,-1,2,-94,-124,-1,2,-94,-126,-1,2,-94,-127,-1,2,-94,-70,-1-1,2,-94,-80,94-1,2,-94,-116,761402-1,2,-94,-118,77183-1,2,-94,-121,;9;-1;1'
}

r = s.post(url, json=sensor_data_1, headers=headers)
print(r)
for c in s.cookies:
	if 'abck' in c.name:
		print(c.value)
		cookie = c.value

sensor_data_2 = {
	'sensor_data': f'7a74G7m23Vrp0o5c9163791.54-1,2,-94,-100,Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0,uaend,11059,20100101,en-US,Gecko,0,0,0,0,390770,761395,5120,1410,5120,1440,1709,1330,3083,,cpen:0,i1:0,dm:0,cwen:0,non:1,opc:0,fc:1,sc:0,wrc:1,isc:105,vib:1,bat:0,x11:0,x12:1,5561,0.746556369373,794095380703.5,loc:-1,2,-94,-101,do_en,dm_en,t_dis-1,2,-94,-105,0,0,0,0,1487,231,0;0,-1,0,1,1627,1627,0;-1,2,-94,-102,0,0,0,0,1487,231,0;0,-1,0,1,1627,1627,0;-1,2,-94,-108,-1,2,-94,-110,-1,2,-94,-117,-1,2,-94,-111,-1,2,-94,-109,-1,2,-94,-114,-1,2,-94,-103,-1,2,-94,-112,https://www.bestbuy.com/-1,2,-94,-115,1,32,32,0,0,0,0,932,0,1588190761407,142,16990,0,0,2831,0,0,934,0,0,{cookie},31911,342,-426645306,26067385-1,2,-94,-106,9,1-1,2,-94,-119,200,0,0,200,200,200,400,200,0,400,0,1000,600,200,-1,2,-94,-122,0,0,0,0,1,0,0-1,2,-94,-123,-1,2,-94,-124,-1,2,-94,-126,-1,2,-94,-127,11133333331333333333-1,2,-94,-70,1544133244;-1753895270;dis;;true;true;true;240;true;24;24;true;false;unspecified-1,2,-94,-80,6454-1,2,-94,-116,761402-1,2,-94,-118,81401-1,2,-94,-121,;3;13;0'
}

r = s.post(url, json=sensor_data_2, headers=headers)
print(r)
for c in s.cookies:
	if 'abck' in c.name:
		print(c.value)

# aj_type = '0,0'								# Type of last device function executed
# browser_bd = 'cpen:0,i1:0,dm:0,cwen:0,non:1,opc:0,fc:1,sc:0,wrc:1,isc:105,vib:1,bat:0,x11:0,x12:1'	# Values 
# navigator_language = 'en-US'				# navigator.language
# navigator_product_sub = '20100101'			# navigator.productSub
# cookie = ''									# Akamai cookie used to create a valid one
# cookie_hash = '31421'						# bmak.ab(bmak.get_cookie())
# d2 = '16990'								# bmak.pi(bmak.z1 / 23)
# d3 = '761395'								# bmak.x2() % 1e7
# derived_api_key = '7a74G7m23Vrp0o5'			# bmak.od(bmak.cs, bmak.api_public_key).slice(0, 16)
# derived_timestamp = '916379'				# Math.floor(bmak.get_cf_date() / 36e5)
# device_events = 'do_en,dm_en,t_dis'			# window.DeviceOrientationEvent, window.DeviceMotionEvent, window.TouchEvent
# dmact = ''									# Related to cdma function (device motions)
# dmevel = '0'								# Related to cdma function (device motions)
# doact = ''									# Related to cdoa function (device orientation)
# doevel = '0'								# Related to cdoa function (device orientation)
# dom_automation = '0'						# window.domAutomation
# form_info = '0,0,0,0,1487,231,0;0,-1,0,1,1627,1627,0;'	# Result from getforminfo function (collects inpuits from the pages and collects the info)
# fp_val_hash = '94'							# bmak.ab(bmak.fpcf.fpValstr)
# fp_val_str = '-1'							# Related to t.data() function (canvas, screen/pixel depth, cookies/location/java enabled, fonts, ect.)
# fpcf_rcfp = ' -1'							# Canvas fingerprinting
# fpcf_rval = '-1'							# Math.floor(1e3 * Math.random()).toString() (Used to make the canvas so it has to math the fingerprint)
# fpcp_td = '-999999'							# Checks how long t.data() took to finish
# d26 = '2831'								# bmak.d2 / 6
# inform_info = '0,0,0,0,1487,231,0;0,-1,0,1,1627,1627,0;'	# Result from getforminfo function (collects inputs from the pages and collects the info)
# init_time = '0'								# Date.now() (related to _setInitTime function)
# inner_height = '1330'						# window.innerHeight || document.body.clientHeight
# inner_width = '1709'						# window.innerWidth || document.body.clientWidth
# kact = ''									# Related to cka function (keydown, keyup, keypress)
# ke_cnt = '0'								# Related to cka function (keydown, keyup, keypress)
# kevel = '1'									# Related to cka function (keydown, keyup, keypress)
# mact = ''									# Related to cma function (mousemove, mouseclick, mousedown, mouseup)
# me_cnt = '0'								# Related to cma function (mousemove, mouseclick, mousedown, mouseup)
# mevel = '32'								# Related to cma function (mousemove, mouseclick, mousedown, mouseup)
# ms_from_start = '2'							# bmak.get_cf_date() - bmak.start_ts
# ms_from_start_2 = '7'
# nck = '0'									# Related to get_cookie (sets to 1 when cookie is found)
# o9 = '761402' 								# bmak.x2() % 1e7
# outer_width = '3083'						# window.outerWidth
# pact = ''									# Related to cpa function (pointerup, pointerdown)
# pe_cnt = '0'								# Counts cpa events
# perf_parms = '-1'							# getmr function - calculates time took to finish math functions
# permissions = ''							# navigator.permissions (Checks state for each)
# pevel = '0'									# Related to cpa function (pointerup, pointerdown)
# phantom = '0'								# window._phantom (Checks for PhantomJS Automation)
# navigator_plugins_length = '0'				# navigator.plugins.length
# navigator_product = 'Gecko'					# navigator.product
# read_doc_url = 'https://www.bestbuy.com/'	# document.URL
# rnd_seem_num = '0.621120255310'				# Random seed number
# screen_avail_height = '1410'				# window.screen.availHeight
# screen_avail_width = '5120'					# window.screen.availWidth
# screen_height = '1440'						# window.screen.height
# screen_width = '5120'						# window.screen.width
# sed = '0,0,0,0,1,0,0'					 	# Checks for webdriver in various ways (navigator, window, document, ect.)
# sensor_data_hash = '77183'					# 24 ^ bmak.ab(bmak.sensor_data)
# start_from_ts = '1588190761395'				# Date.now()
# start_ts_2 = '794095380697.5'				# Date.now() / 2
# ta = '0'									# Counter for various events
# tact = ''									# Related to cta function (touchmove, touchstart, touchend, touchcancel)
# te_cnt = '0'								# Counts cta events
# tevel = '32'								# Related to cta function (touchmove, touchstart, touchend, touchcancel)
# timings = ';9;-1;1'							# Timings related to execution of main sensor gen function
# ua_hash = '5561'							# bmak.ab(window.navigator.userAgent.replace(/\|"/g, ""))
# window_navigator_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'	# window.navigator.userAgent
# vcact = ''									# Related to lvc function (visibilitychange, onblur, onfocus)
# vel_sum = '0'								# bmak.ke_vel + bmak.me_vel + bmak.doe_vel + bmak.dme_vel + bmak.te_vel + bmak.pe_vel
# akamai_version = '1.54'						# bmak.ver
# web_driver = '0'							# window.webdriver
# xagg = '11059'								# Relatedd to bc function, checks various browser native functions
# z1 = '390770'								# bmak.pi(bmak.start_ts / (2016 * 2016))

# separator = '-1,2,-94,'

# sensor_data = f'{derived_api_key}c{derived_timestamp}{akamai_version}{separator}-100,{window_navigator_user_agent},uaend,{xagg},{navigator_product_sub},{navigator_language},{navigator_product},{navigator_plugins_length},{phantom},{web_driver},{dom_automation},{z1},{d3},{screen_avail_width},{screen_avail_height},{screen_width},{screen_height},{inner_width},{inner_height},{outer_width},,{browser_bd},{ua_hash},{rnd_seem_num},{start_ts_2},loc:{separator}-101,{device_events}{separator}-105,{inform_info}{separator}-102,{form_info}{separator}-108,{separator}-110,{separator}-117,{separator}-111,{separator}-109,{separator}-114,{separator}-103,{separator}-112,{read_doc_url}{separator}-115,{kevel},{mevel},{tevel},{doevel},{dmevel},{pevel},{vel_sum},{ms_from_start},{init_time},{start_from_ts},{fpcp_td},{d2},{ke_cnt},{me_cnt},{d26},{pe_cnt},{te_cnt},{ms_from_start_2},{ta},{nck},{cookie},{cookie_hash},{fpcf_rval},{fpcf_rcfp},26067385{separator}-106,{aj_type}{separator}-119,{perf_parms}{separator}-122,{sed},{separator}-123,{separator}-124,{separator}-126,{separator}-127,{separator}-70,{fp_val_str}{separator}-80,{fp_val_hash}{separator}-116,{o9}{separator}-118,{sensor_data_hash}{separator}-121,{timings}'