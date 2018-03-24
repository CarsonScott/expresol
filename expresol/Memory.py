class Memory:	
	def __init__(self, size):
		self.store = list()
		self.table = dict()
		for i in range(size):
			self.store.append(Data())
	def set_data(self, index, value):
		Set(self.store[index], value)
	def get_data(self, index):
		return Get(self.store[index])
	def get_variable(self, name):
		return self.table[name]
	def set_variable(self, name, index, type):
		self.table[name] = Variable(name, Reference(index, self.store), type)

class Operator:
	def __init__(self, function=None, inputs=[]):
		self.inputs = inputs
		self.function = function
	def __call__(self):
		return self.function(self.inputs)

def Data(value=None, type=None):
	y = dict()
	y['type'] = type
	y['value'] = value
	return y
def Reference(index=None, memory=None):
	y = Data(memory[index], 'reference')
	y['index'] = index
	return y
def Variable(name=None, reference=None, subtype=None):
	y = Data(reference, 'variable')
	y['class'] = subtype
	y['name'] = name
	return y
def Get(data):
	return data['value']
def Set(data, value):
	data['value'] = value
	return data
def Type(data):
	return data['type']
def Index(data):
	return data['index']
def Name(data):
	return data['name']
def Class(data):
	return data['class']