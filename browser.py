from PyQt5 import QtWidgets, QtCore, QtGui

class Browser(QtWidgets.QFrame):

	def __init__(self, browser_id):
		QtWidgets.QFrame.__init__(self)
		self.browser_id = browser_id