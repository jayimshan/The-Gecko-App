from PyQt5.QtCore import QThread, pyqtSignal
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def funkoshop():
	sitekey = '6LeoeSkTAAAAAA9rkZs5oS82l69OEYjKRZAiKdaF'
	# sitekey = '6LcCR2cUAAAAANS1Gpq_mDIJ2pQuJphsSQaUEuc9'
	return render_template('recaptcha.html', sitekey=sitekey)

# @app.route('/')
# def hottopic():
# 	sitekey = '6LdasBsTAAAAAJ2ZY_Z60WzgpRRgZVKXnqoad77Y'
# 	return render_template('recaptcha.html', sitekey=sitekey)

@app.route('/<store>')
def recaptcha(store):
	print(store)
	if store == 'funkoshop':
		return funkoshop()
	elif store == 'hottopic':
		return hottopic()
	else:
		return 'Error, contact admin'

class LocalServer(QThread):

	def __init__(self):
		QThread.__init__(self)

	def stop(self):
		print('Stopping server')
		self.quit()

	def run(self):
		print('Running server')
		# app.run(ssl_context='adhoc')
		app.run()