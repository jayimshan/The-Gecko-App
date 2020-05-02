import queue

class CaptchaQueue:

	def __init__(self):
		self.q = queue.Queue()

	def get_token(self):
		if not self.q.empty():
			return self.q.get()
		else:
			return None