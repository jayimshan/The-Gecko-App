from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtWidgets, QtCore, QtGui, QtWebEngineWidgets, QtWebChannel, QtWebEngineCore, QtNetwork
import browser
import webpage

import time

class Solver(QThread):

	request_token = pyqtSignal(int)
	request_element = pyqtSignal(int)
	add_token = pyqtSignal(str, str)

	def __init__(self, solver_id, solver_name):
		QThread.__init__(self)
		self.solver_id = solver_id
		self.solver_name = solver_name
		self.sitekey = None
		# self.url = 'http://gecko.hottopic.com:3000'

		# self.solver = browser.Browser(solver_id)
		# self.solver = QtWebEngineWidgets.QWebEngineView()
		self.solver = webpage.Webpage()
		# self.solver.load_finished.connect(self.load_page)
		# self.settings = QtWebEngineWidgets.QWebEngineSettings.defaultSettings()
		# self.settings.setAttribute(QtWebEngineWidgets.QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
		# self.page = webpage.Webpage()
		# self.solver.setPage(self.page)
		# self.cookie_store = self.page.profile().cookieStore()

		# self.solver.page().load(QtCore.QUrl(self.url))
		self.abort = False
		self.load_finished = False
		self.script_load = False
		self.show_solver = False
		# self.solver.page().loadFinished.connect(self.loaded)
		# self.solver.page().contentSizeChanged.connect(self.resize_page)
		self.token = None
		self.available = True
		self.store_name = None

		# self.frame = QtWidgets.QFrame()
		self.frame = browser.Browser(self.solver_id)
		self.layout = QtWidgets.QVBoxLayout(self.frame)
		self.label_gif = QtWidgets.QLabel()
		self.label = QtWidgets.QLabel()
		self.label.setText('Waiting for captcha')
		self.layout.addWidget(self.solver, alignment=QtCore.Qt.AlignCenter)
		self.layout.addWidget(self.label_gif, alignment=QtCore.Qt.AlignCenter)
		self.layout.addWidget(self.label, alignment=QtCore.Qt.AlignCenter)
		self.loading_gif = QtGui.QMovie('gifs/loading.gif')
		self.label_gif.setMovie(self.loading_gif)
		# self.load_waiting()
		self.start()

	# def set_cookies(self, cookies):
	# 	for cookie in cookies:
	# 		print('name: {}'.format(cookie.name()))
	# 		print('value: {}'.format(cookie.value()))
	# 		print('domain: {}'.format(cookie.domain()))
	# 		self.solver.page().profile().cookieStore().setCookie(cookie)

	def load_page(self, url):
		print('Loading page')
		self.solver.page.loadFinished.connect(self.load_script)
		self.load_captcha()
		self.solver.page.load(QtCore.QUrl(url))

	def load_script(self):
		print('Loading script')
		script = '''
		document.write("<head><script src=https://www.google.com/recaptcha/api.js async defer></script></head><body><div class=g-recaptcha id=test data-sitekey={} render=explicit></div></body>")
		'''.format(self.sitekey)
		self.solver.page.runJavaScript(script, self.show)
		self.script_load = True

	def show(self, data):
		print('js callback')

	def get_element(self):
		print('getting element')
		# load = '''
		# grecaptcha.render(document.getElementById('test'))
		# '''
		load = '''
		document.getElementById('test')
		'''
		self.solver.page.runJavaScript(load, self.test_2)

	def test_2(self, data):
		print(data)
		if type(data) is dict:
			print('dict')
			load = '''
			grecaptcha.render(document.getElementById('test'))
			'''
			print('loading script')
			self.solver.page.runJavaScript(load)
			print('setting vars')
			self.script_load = False
			self.show_solver = True
			self.load_finished = True
			# self.load_captcha()
			# self.load_waiting()
		else:
			print('Still rendering')

	def load_captcha(self):
		self.available = False
		self.solver.show()
		self.solver.setGeometry(0, 0, 380, 600)
		# self.layout.addWidget(self.solver, alignment=QtCore.Qt.AlignCenter)
		# self.solver.page().load(QtCore.QUrl('https://accounts.google.com'))
		# self.solver.page().load(QtCore.QUrl(url))
		# self.solver.load_page(url)
		# self.solver.load()
		self.loading_gif.stop()
		self.label_gif.hide()
		self.label.hide()

	def load_waiting(self):
		self.available = True
		self.load_finished = False
		self.store_name = None
		# self.solver.hide()
		# self.layout.removeWidget(self.solver)
		self.solver.hide()
		self.solver.setGeometry(0, 0, 0, 0)
		self.loading_gif.start()
		self.label_gif.show()
		self.label.show()

	def get_token(self):
		print('Attempting to get token')
		# self.solver.page().runJavaScript("document.getElementById('g-recaptcha-response').value;", self.print_captcha)
		self.solver.page.runJavaScript("grecaptcha.getResponse();", self.print_captcha)
		# self.solver.page().runJavaScript("document.getElementById('my_form').addEventListener('submit', function(evt) {var response = grecaptcha.getResponse();});", self.print_captcha)

	def print_captcha(self, value):
		if value:
			if len(value) > 0:
				self.add_token.emit(self.store_name, value)
				# self.abort = True
				# self.quit()
				self.load_waiting()
			else:
				print('Nothing')

	def loaded(self):
		self.load_finished = True

	def stop_solver(self):
		self.abort = True
		self.quit()

	def run(self):
		while not self.abort:
			if self.script_load:
				self.request_element.emit(self.solver_id)
			if self.show_solver:
				# self.load_captcha()
				self.show_solver = False
			if self.load_finished:
				self.request_token.emit(self.solver_id)
			self.msleep(1000)