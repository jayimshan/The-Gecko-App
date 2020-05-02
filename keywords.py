

class Keyword:

	def __init__(self, pos_kw, neg_kw):
		self.pos_kw = pos_kw
		self.neg_kw = neg_kw

	def get_lower(self, split_method):
		pos = []
		neg = []
		split = ' '
		if split_method == 'Comma':
			split = ','
		if self.pos_kw:
			for kw in self.pos_kw.split(split):
				pos.append(kw.lower())
		if self.neg_kw:
			for kw in self.neg_kw.split(split):
				neg.append(kw.lower())
		keywords = {
			'pos': pos,
			'neg': neg
		}
		return keywords