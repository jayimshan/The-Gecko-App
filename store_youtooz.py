from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import QtCore, QtNetwork
from bs4 import BeautifulSoup
from webhook import Webhook
from webpage import Webpage

import requests
import random
import json
import time
import urllib.parse

class Youtooz(QObject):

	store = 'https://youtooz.com/'

	# s = requests.Session()

	def __init__(self, s, task_type, captcha_logic, keywords, size, qty, profile, billing):
		QObject.__init__(self)
		self.title = None
		self.src = None
		self.variant_id = None
		self.authenticity_token = None
		self.shipping_code = None
		self.checkout_price = None

		self.s = s
		self.task_type = task_type
		self.captcha_logic = captcha_logic
		self.keywords = keywords
		self.size = size
		self.qty = qty
		self.profile = profile
		self.billing = billing
		self.token = None
		self.size_emit = None
		
		self.page = Webpage()
		self.cookies = []
		self.client_width = None
		self.client_height = None
		self.random_client_resolution()
		self.waiting_for_captcha = False
		self.abort = False

		self.status = {
			'search_all_products': False,
			'add_to_cart': False,
			'start_checkout': False,
			'submit_info': False,
			'submit_shipping': False,
			'submit_payment': False,
			'checkout_successful': False
		}