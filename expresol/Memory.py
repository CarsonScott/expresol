from .Data import *

class Memory:	
	def __init__(self, size):
		self.store = list()
		self.table = dict()
		for i in range(size):
			self.store.append(Data())
	
	def get_data(self, index):
		return Get(self.store[index])
	
	def set_data(self, index, value):
		Set(self.store[index], value)
	
	def get_variable(self, name):
		return self.table[name]
	
	def set_variable(self, name, index, type):
		pointer = Reference(index, self.store)
		self.table[name] = Variable(name, pointer, type)