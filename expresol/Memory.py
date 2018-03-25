from .Data import *

class Memory:	
	def __init__(self, size):
		self.store = list()
		self.table = dict()
		for i in range(size):
			self.store.append(None)
	
	def dat(self, index, value):
		self.store[index] = Data(value)
	
	def var(self, name, index, type):
		self.table[name] = Variable(name, index, type)

	def get_var(self, name):
		var = self.table[name]
		return var

	def get_dat(self, index):
		dat = self.store[index]
		return dat