from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtWidgets

import requests

class Token(QThread):

	status_updated = pyqtSignal(str, QtWidgets.QTableWidgetItem)
	retry_updated = pyqtSignal(int, QtWidgets.QTableWidgetItem)
	life_updated = pyqtSignal(int, QtWidgets.QTableWidgetItem)
	log_updated = pyqtSignal(str, QtWidgets.QTableWidgetItem)
	expired = pyqtSignal(QtWidgets.QTableWidgetItem)
	ready = pyqtSignal()

	def __init__(self, store, proxy, delay):
		QThread.__init__(self)

		self.store = store
		self.proxy = proxy
		self.delay = delay
		self.status = 'Submitting challenge'
		self.retry = 20
		self.life = 0
		self.api_key = 'ee5d7a0260ab239c83099cc055be5261'
		self.url = 'https://www.hottopic.com'
		self.sitekey = '6LdasBsTAAAAAJ2ZY_Z60WzgpRRgZVKXnqoad77Y'
		self.method = 'userrecaptcha'
		self.post = 'http://2captcha.com/in.php?key={}&method={}&googlekey={}&pageurl={}&json=1'.format(self.api_key, self.method, self.sitekey, self.url)
		self.token = None
		self.abort = False

		self.widget_store = QtWidgets.QTableWidgetItem(self.store)
		self.widget_proxy = QtWidgets.QTableWidgetItem(self.proxy)
		self.widget_status = QtWidgets.QTableWidgetItem(self.status)
		self.widget_retry = QtWidgets.QTableWidgetItem(self.retry)
		self.widget_life = QtWidgets.QTableWidgetItem(self.life)

	def run(self):
		# initial sleep (interval per captcha request)
		self.msleep(self.delay)
		# try:
		# 	response = requests.get(self.post)
		# 	status = response.json()['status']
		# 	request = response.json()['request']
		# 	if status == 1:
		# 		self.get = 'https://2captcha.com/res.php?key={}&action=get&id={}&json=1'.format(self.api_key, request)
		# 	else:
		# 		if request == 'ERROR_WRONG_USER_KEY':
		# 			self.status = 'ERROR_WRONG_USER_KEY'
		# 		elif request == 'ERROR_KEY_DOES_NOT_EXIST':
		# 			self.status = 'ERROR_KEY_DOES_NOT_EXIST'
		# 		elif request == 'ERROR_ZERO_BALANCE':
		# 			self.status = 'ERROR_ZERO_BALANCE'
		# 		elif request == 'ERROR_NO_SLOT_AVAILABLE':
		# 			self.status = 'ERROR_NO_SLOT_AVAILABLE'
		# 		elif request == 'IP_BANNED':
		# 			self.status = 'IP_BANNED'
		# 		elif request == 'ERROR_BAD_TOKEN_OR_PAGEURL':
		# 			self.status = 'ERROR_BAD_TOKEN_OR_PAGEURL'
		# 		elif request == 'ERROR_GOOGLEKEY':
		# 			self.status = 'ERROR_GOOGLEKEY'
		# 		elif request == 'MAX_USER_TURN':
		# 			self.status = 'MAX_USER_TURN'
		# 		else:
		# 			self.status = request
		# 		self.status_updated.emit(self.status, self.row)
			
		# except Exception as e:
		# 	self.log_updated.emit(str(e), self.row)

		# while self.retry > 0:
		# 	self.retry_updated.emit(self.retry, self.row)
		# 	self.retry -= 1
		# 	self.sleep(1)

		# for i in range(0, 15):
		# 	response = requests.get(self.get)
		# 	status = response.json()['status']
		# 	request = response.json()['request']
		# 	self.retry = 6
		# 	if status == 1:
		# 		self.token = request
		# 		self.status = 'Ready'
		# 		self.status_updated.emit(self.status, self.row)
		# 		self.retry = -1
		# 		self.retry_updated.emit(self.retry, self.row)
		# 		self.life = 10
		# 		self.life_updated.emit(self.life, self.row)
		# 		break
		# 	else:
		# 		if request == 'CAPCHA_NOT_READY':
		# 			self.status = 'CAPTCHA_NOT_READY'
		# 		elif request == 'ERROR_CAPTCHA_UNSOLVABLE':
		# 			self.status = 'ERROR_CAPTCHA_UNSOLVABLE'
		# 		elif request == 'ERROR_WRONG_USER_KEY':
		# 			self.status = 'ERROR_WRONG_USER_KEY'
		# 		elif request == 'ERROR_KEY_DOES_NOT_EXIST':
		# 			self.status = 'ERROR_KEY_DOES_NOT_EXIST'
		# 		elif request == 'ERROR_WRONG_ID_FORMAT':
		# 			self.status = 'ERROR_WRONG_ID_FORMAT'
		# 		elif request == 'ERROR_WRONG_CAPTCHA_ID':
		# 			self.status = 'ERROR_WRONG_CAPTCHA_ID'
		# 		elif request == 'ERROR: 1001':
		# 			self.status = 'Too many requests: wait 10 minutes'
		# 		elif request == 'ERROR: 1002':
		# 			self.status = 'Too many requests: wait 5 minutes'
		# 		elif request == 'ERROR: 1003':
		# 			self.status = 'Too many requests: wait 30 seconds'
		# 		elif request == 'ERROR: 1004':
		# 			self.status = 'Too many requests: wait 10 minutes'
		# 		elif request == 'ERROR: 1005':
		# 			self.status = 'Too many requests: wait 5 minutes'
		# 		elif request == 'MAX_USER_TURN':
		# 			self.status = 'Too many requests: wait 10 seconds'
		# 		else:
		# 			self.status = request
		# 		self.status_updated.emit(self.status, self.row)
		# 		self.retry_updated.emit(self.retry, self.row)

		# 		while self.retry > 0:
		# 			self.retry -= 1
		# 			self.sleep(1)
		# 			self.retry_updated.emit(self.retry, self.row)

		self.life = 10
		while self.life > 0:
			if self.life == 5:
				self.ready.emit()
			self.life -= 1
			self.sleep(1)
			self.life_updated.emit(self.life, self.widget_life)
		# self.status_updated.emit('Expired')
		self.sleep(1)
		self.expired.emit(self.widget_store)