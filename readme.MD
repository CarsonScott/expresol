# expresol

A flexible library for creating script-languages in python

__EXAMPLE CODE__:

- import library
	from expresol import Memory, Parser

- create memory with 10 elements

	memory = Memory(10)

- store functions and data in memory

	memory.set_data(0, AND)
	memory.set_data(1, OR)
	memory.set_data(2, True)
	memory.set_data(3, True)
	memory.set_data(4, False)

- store grammatical labels in memory

	memory.set_data(5, 'open')
	memory.set_data(6, 'close')
	memory.set_data(7, 'end')

- assign variable symbols to elements

	memory.set_variable('&', 0, 'operator')
	memory.set_variable('|', 1, 'operator')
	memory.set_variable('a', 2, 'data')
	memory.set_variable('b', 3, 'data')
	memory.set_variable('c', 4, 'data')
	memory.set_variable('(', 5, 'grammar')
	memory.set_variable(')', 6, 'grammar')
	memory.set_variable(';', 7, 'grammar')

- create parser

	parser = Parser()

- define symbol types

	parser.add_type('grammar','();')
	parser.add_type('number','1234567890')
	parser.add_type('operator','&|!+-*/=')
	parser.add_type('data','abcdefghijklmnopqrstuvwxyz')


- store valid consequtive pairs of symbol types

	parser.add_rule(('operator','operator'))
	parser.add_rule(('grammar','none'))
	parser.add_rule(('none','grammar'))
	parser.add_rule(('data','number'))
	parser.add_rule(('data','data'))

- execute statement

	statement = '(a & b);'
	output = parser(statement, memory)
