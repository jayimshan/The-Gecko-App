from PyQt5 import QtCore, QtGui, QtWidgets

class Proxy():

	def __init__(self, proxy_id, proxy_name, proxies):
		self.proxy_id = proxy_id
		self.proxy_name = proxy_name
		self.proxies = proxies
		# self.length = self.proxies.split('\n')
		self.buttons = []
		self.button_widgets = []
		for item in self.proxies.split('\n'):
			button = QtWidgets.QPushButton('Test')
			button.setMinimumHeight(20)
			self.buttons.append(button)
			layout = QtWidgets.QHBoxLayout()
			layout.addWidget(button)
			widget = QtWidgets.QWidget()
			widget.setLayout(layout)
			self.button_widgets.append(widget)

		self.test_proxy()

	def test_proxy(self):
		for button in self.buttons:
			button.clicked.connect(self.test)

	def test(self):
		print('lalala')