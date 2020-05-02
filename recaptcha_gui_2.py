from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from recaptcha_ui import Ui_Form
from webview import Webview

import queue

class RecaptchaGUI(QtWidgets.QWidget):

	def __init__(self):
		super().__init__()
		# QtWidgets.QWidget.__init__(self, parent)
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		image_add_tab = QtGui.QPixmap('icons/icon_add.png')
		image_add = QtGui.QPixmap('icons/icon_add_2.png')
		image_trash = QtGui.QPixmap('icons/icon_trash.png')
		icon_add_tab = QtGui.QIcon(image_add_tab)
		icon_add = QtGui.QIcon(image_add)
		icon_trash = QtGui.QIcon(image_trash)

		self.ui.push_button_new_tab.setIcon(icon_add_tab)
		self.ui.push_button_add.setIcon(icon_add)
		self.ui.push_button_delete.setIcon(icon_trash)
		self.ui.tab_widget.setCornerWidget(self.ui.push_button_new_tab)

		# self.ui.push_button_new_tab.clicked.connect(lambda: self.create_solver.emit())
		self.ui.push_button_new_tab.clicked.connect(self.add_tab)
		self.ui.tab_widget.tabCloseRequested.connect(self.remove_tab)

		self.tabs = queue.Queue()

		self.add_tab()

	def add_tab(self):
		tab_name = 'Tab'
		browser = Webview()
		self.tabs.put(browser)
		# browser.show()
		browser.load_url('https://colourpop.com')
		self.ui.tab_widget.addTab(browser, tab_name)
		# self.start_solver.emit(solver.solver_id)

	def remove_tab(self, index):
		# solver_id = self.ui.tab_widget.widget(index).browser_id
		self.ui.tab_widget.removeTab(index)
		# self.delete_solver.emit(solver_id)

	# def remove_tabs(self):
	# 	i = 0
	# 	tab_count = self.ui.tab_widget.count()
	# 	while i < tab_count:
	# 		self.ui.tab_widget.removeTab(0)
	# 		i += 1

	# def closeEvent(self, event):
	# 	self.remove_tabs()
	# 	self.stop_solvers.emit()
