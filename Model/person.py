class Person(object):
	"""docstring for MC"""
	def __init__(self, name,expa_id=0,espo_id=0):
		super(Person, self).__init__()
		self.name = name
		self.expa_id = expa_id
		self.espo_id = espo_id
	