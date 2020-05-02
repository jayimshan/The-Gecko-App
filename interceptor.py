from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets, QtWebEngineCore
from PyQt5.QtWebEngineCore import QWebEngineUrlRequestInterceptor
from PyQt5.QtCore import pyqtSignal

class Interceptor(QWebEngineUrlRequestInterceptor):

	def __init__(self, headers):
		super().__init__()
		self.headers = headers
		# self.once = False

	def interceptRequest(self, info):
		# print('info: {}'.format(info.resourceType()))
		# info.setHttpHeader(b'Access-Control-Allow-Origin', b'*')
		# print(info.firstPartyUrl())
		# print(info.requestUrl())
		# if 'shop.funko.com' in str(info.requestUrl()):
			# print('Blocking request to {}'.format(info.requestUrl()))
			# info.block(True)
			# print('userverify')
		if 'https://mail.google.com/' in info.requestUrl().url():
			print('Setting user-agent')
			for key, value in self.headers.items():
				info.setHttpHeader(bytes(key, 'utf-8'), bytes(value, 'utf-8'))
			# info.setHttpHeader(QtCore.QByteArray().append(key), QtCore.QByteArray().append(value))
		# if 'funko' in info.firstPartyUrl().toString():
		# info.redirect(QtCore.QUrl.fromLocalFile(QtCore.QFileInfo('test.html').absoluteFilePath()))
		# print(QtCore.QUrl.fromLocalFile(QtCore.QFileInfo('test.html').absoluteFilePath()))
			# if not self.once:
			# 	self.test.emit()
			# 	self.once = True
			# info.redirect(QtCore.QUrl.fromLocalFile('/test.html'))
		# print('headers: {}'.format(self.headers))