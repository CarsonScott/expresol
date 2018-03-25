from .Data import *

class Memory:	
	def __init__(self, size):
		self.store = list()
		self.table = dict()
		for i in range(size):
			self.store.append(None)
	
	def var(self, index, value):
		self.store[index] = Variable(value)
	
	def ref(self, index, symbol, datatype):
		self.table[symbol] = Reference(index, symbol, datatype)

	def get(self, obj):
		if isinstance(obj, str):
			obj = self.table[obj]
		if isinstance(obj, Reference):
			index = obj['index']
			var = self.store[index]
			obj['value'] = var['value']
		return obj
			