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
