from PyQt5 import QtCore
from PyQt5.QtCore import QUrl, pyqtSignal
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView, QWebEngineProfile
from PyQt5.QtNetwork import QNetworkCookie
# from interceptor import Interceptor

import time

class Webpage(QWebEngineView):

	load_finished = pyqtSignal(QtCore.QByteArray)

	def __init__(self):
		super().__init__()
		# QWebEngineView.__init__(self)
		# self.interceptor = Interceptor()
		self.profile = QWebEngineProfile(self)
		self.cookie_store = self.profile.cookieStore()
		self.cookie_store.cookieAdded.connect(self.on_cookie_added)
		self.page = QWebEnginePage(self.profile, self)
		# self.page.profile().setUrlRequestInterceptor(self.interceptor)
		self.setPage(self.page)
		self.cookies = []
		self.loadFinished.connect(self.get_cookies)
		self.show()
		# self.page().profile().setUrlRequestInterceptor(self.interceptor)
		# self.page().loadFinished.connect(self.load_script)
		# self.manager = QNetworkAccessManager()
		# self.request = QtNetwork.QNetworkRequest()
		# self.request.setUrl(QtCore.QUrl('https://shop.funko.com'))
		self.html = None
		# self.load_finished = False
		self.r = None
		# for cookie in cookies:
		# 	print('name: {}'.format(cookie.name()))
		# 	print('value: {}'.format(cookie.value()))
		# 	print('domain: {}'.format(cookie.domain()))
		# 	self.page().profile().cookieStore().setCookie(cookie)
		# self.loadFinished.connect(self.on_load_finished)
		# self.load(QUrl(url))

	def load_url(self, url):
		self.load(QUrl(url))

	def on_cookie_added(self, cookie):
		for c in self.cookies:
			if c.hasSameIdentifier(cookie):
				return
		self.cookies.append(QNetworkCookie(cookie))

	def set_cookies(self, cookies):
		for cookie in cookies:
			# print('name: {}'.format(cookie.name()))
			# print('value: {}'.format(cookie.value()))
			# print('domain: {}'.format(cookie.domain()))
			self.page.profile().cookieStore().setCookie(cookie)

	def get_cookies(self):
		for cookie in self.cookies:
			print('[DOMAIN] {}'.format(cookie.domain()))
			print('[NAME] {}'.format(cookie.name()))
			print('[VALUE] {}'.format(cookie.value()))
			print()

	# def load_page(self, url):
	# 	self.page().load(QUrl(url))

	# def load_script(self):
	# 	script = '''
	# 	document.write("<script src=https://www.google.com/recaptcha/api.js async defer></script></head>")
	# 	'''
	# 	self.page().runJavaScript(script, self.load_div)

	# def load_div(self, data):
	# 	time.sleep(3)
	# 	div = '''
	# 	document.write("<div class=g-recaptcha id=test data-sitekey=6LeoeSkTAAAAAA9rkZs5oS82l69OEYjKRZAiKdaF render=explicit></div>")
	# 	'''
	# 	self.page().runJavaScript(div, self.load_test)

	# def load_test(self, data):
	# 	time.sleep(3)
	# 	load = '''
	# 	grecaptcha.render(document.getElementById('test'));
	# 	'''
	# 	self.page().runJavaScript(load)

	def on_load_finished(self):
		print('Called')
		self.page().toHtml(self.callable)
		# self.load_finished = True
		print('Load finished')

	def callable(self, data):
		self.html = data
		# self.show()
		print('Print finished')

	# def acceptNavigationRequest(self, url, _type, isMainFrame):
	# 	if _type == QWebEnginePage.NavigationTypeLinkClicked:
	# 		self.setUrl(url)
	# 		print(url)
	# 		return False
	# 	return True

	# def certificateError(self, error):
	# 	# print(error)
	# 	return True