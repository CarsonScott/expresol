class Marker(dict):
	def __init__(self, label):
		self['label'] = label

class Operator(dict):
	def __init__(self, function=None, inputs=[]):
		self['function'] = function
		self['inputs'] = inputs
	def __call__(self, inputs):
		self['inputs'] = inputs
		return self.compute()
	def compute(self):
		return self['function'](self['inputs'])

class Variable(dict):
	def __init__(self, value=None):
		self['value'] = value

class Pointer(dict):
	def __init__(self, symbol=None, index=None):
		self['symbol'] = symbol
		self['index'] = index

class Reference(dict):
	def __init__(self, index=None, symbol=None, datatype=None, value=None):
		self['symbol'] = symbol
		self['index'] = index
		self['type'] = datatype
		self['value'] = value

		
