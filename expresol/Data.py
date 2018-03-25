def Data(value=None, type=None):
	y = dict()
	y['type'] = type
	y['value'] = value
	return y

def Variable(name=None, index=None, type=None):
	y = Data(index, 'variable')
	y['name'] = name
	y['class'] = type
	return y

def Get(data):
	return data['value']

def Set(data, value):
	data['value'] = value
	return data

def Type(data):
	return data['type']

def Name(data):
	return data['name']

def Class(data):
	return data['class']
