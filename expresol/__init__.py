from .Memory import Memory
from .Parser import Parser
from .Data import Marker, Operator

def TRUE(X):	
	if len(X) != 1:raise Exception()
	return X[0] == True
def FALSE(X):
	if len(X) != 1:raise Exception()
	return X[0] == False
def NOT(X):
	if len(X) != 1:raise Exception()
	return not X[0]
def AND(X):
	if len(X) != 2:raise Exception()
	return X[0] and X[1]	
def OR(X):
	if len(X) != 2:raise Exception()
	return X[0] or X[1]
def EQ(X):
	if len(X) != 2:raise Exception()
	return X[0] == X[1]
def MT(X):
	if len(X) != 2:raise Exception()
	return X[0] > X[1]
def LT(X):
	if len(X) != 2:raise Exception()
	return X[0] < X[1]
def ADD(X):
	if len(X) != 2:raise Exception()
	return X[0] + X[1]
def SUB(X):
	if len(X) != 2:raise Exception()
	return X[0] - X[1]
def MULT(X):
	if len(X) != 2:raise Exception()
	return X[0] * X[1]
def DIV(X):
	if len(X) != 2:raise Exception()
	return X[0] / X[1]
def LEN(X):
	if len(X) != 1: raise Exception()
	return len(X[0])
def ID(X):
	if len(X) != 1: raise Exception()
	return X[0]
def GET(X):
	if len(X) != 2: raise Exception()
	return X[0][X[1]]
def SET(X):
	if len(X) != 3: raise Exception()
	X[0][X[1]] = X[2]
def CALL(X):
	if len(X) != 2: raise Exception()
	return X[0](X[1])