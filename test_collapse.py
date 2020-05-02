from test_collapse_ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

import sys

class MainWindowExec():

	def __init__(self):
		app = QtWidgets.QApplication(sys.argv)
		MainWindow = QtWidgets.QMainWindow()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(MainWindow)

		self.ui.checkBox.stateChanged.connect(self.test)

		MainWindow.show()
		sys.exit(app.exec_())

	def test(self):
		if self.ui.checkBox.isChecked():
			self.ui.tableWidget.show()
		else:
			self.ui.tableWidget.hide()

if __name__ == "__main__":
	MainWindowExec()