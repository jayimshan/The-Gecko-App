from PyQt5.QtCore import QThread, pyqtSignal
from mitmproxy import proxy, options
from mitmproxy.tools.dump import DumpMaster
from mitmproxy.addons import core

import requests

class AddHeader:

	def __init__(self):
		self.num = 0

	def response(self, flow):
		self.num = self.num + 1
		print(self.num)
		flow.response.headers['count'] = str(self.num)

addons = [
	AddHeader()
]

# opts = options.Options(listen_host='127.0.0.1', listen_port=8080)
# pconf = proxy.config.ProxyConfig(opts)

# m = DumpMaster(None)
# m.server = proxy.server.ProxyServer(pconf)
# m.addons.add(addons)

class Testing:

	def __init__(self):
		opts = options.Options(listen_host='127.0.0.1', listen_port=8080)
		pconf = proxy.config.ProxyConfig(opts)
		self.m = DumpMaster(None)
		self.m.server = proxy.server.ProxyServer(pconf)
		self.m.addons.add(addons)
		# self.m.addons.add(core.Core())

	def run(self):
		self.m.run()
		print('running')

	def stop(self):
		self.m.shutdown()
		print('shutting down')
# print(m.addons)