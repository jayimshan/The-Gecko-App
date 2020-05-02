from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtWidgets, QtCore, QtGui

import http.server
import socketserver

# html = """
# 	<!DOCTYPE html>
# 	<html>
# 		<head>
# 			<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
# 			<script src="https://www.google.com/recaptcha/api.js" async defer></script>
# 		</head>
# 		<body>
# 			<form action="/app.js" method="POST">
# 				<div class="g-recaptcha" data-sitekey="{}"></div>
# 			</form>
# 		</body>
# 	</html>
# """.format('6LdasBsTAAAAAJ2ZY_Z60WzgpRRgZVKXnqoad77Y')

# Hottopic: 6LdasBsTAAAAAJ2ZY_Z60WzgpRRgZVKXnqoad77Y
# Funkoshop: 6LeoeSkTAAAAAA9rkZs5oS82l69OEYjKRZAiKdaF

# class MyHandler(http.server.BaseHTTPRequestHandler):
# 	def do_GET(self):
# 		self.send_response(200)
# 		self.send_header('Content-type', 'text/html')
# 		self.end_headers()
# 		self.wfile.write(bytes(html, 'utf-8'))
# 		self.wfile.close()

class MyHandler(http.server.BaseHTTPRequestHandler):

	def __init__(self, html):
		self.html = html

	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		self.wfile.write(bytes(self.html, 'utf-8'))
		self.wfile.close()

class LocalServer(QThread):

	def __init__(self, sitekey):
		QThread.__init__(self)
		self.port = 3000
		self.html = """
			<!DOCTYPE html>
			<html>
				<head>
					<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
					<script src="https://www.google.com/recaptcha/api.js" async defer></script>
				</head>
				<body>
					<form action="/app.js" method="POST">
						<div class="g-recaptcha" data-sitekey="{}"></div>
					</form>
				</body>
			</html>
		""".format(sitekey)
		self.handler = MyHandler(self.html)
		self.httpd = socketserver.TCPServer(('127.0.0.1', self.port), self.handler)
		print('Serving at port', self.port)

	def stop(self):
		print('Shutting down server')
		self.httpd.shutdown()
		self.quit()

	def run(self):
		print('Starting server')
		self.httpd.serve_forever()