# expresol

Expresol is an easy-to-use python library for creating, translating and executing statements in a user-defined language. The expresol library contains two main parts, namely the memory and the parser. Each contributes differently to the process of translating and then executing the instructions given by a statement.

---

__EXAMPLE CODE__:

- import library and create memory with 10 elements
        
        from expresol import *
        memory = Memory(10)

- store functions, data, and syntax markers in memory  

        memory.dat(0, True)
        memory.dat(1, True)
        memory.dat(2, AND)
        memory.var(3, Marker('open'))
        memory.var(4, Marker('close'))
        memory.var(5, Marker('end'))

- assign symbols to elements that allow data to be accessed when observed in a statement 

        memory.var('x1', 0, 'data')
        memory.var('x2', 1, 'data')
        memory.var('&', 2, 'operator')
        memory.var('(', 3, 'grammar')
        memory.var(')', 4, 'grammar')
        memory.var(';', 5, 'grammar')

- create parser and store data types with characters that are used to form valid symbols for instances of each type

        parser = Parser()
        parser.type('grammar', '();')
        parser.type('operator', '&|!+-*/=')
        parser.type('number', '1234567890')
        parser.type('data', 'abcdefghijklmnopqrstuvwxyz')

- store pairs of data types that reflect the valid transitions between consecutive elements in a statement

        parser.rule('operator','operator')
        parser.rule('grammar','none')
        parser.rule('none','grammar')
        parser.rule('data','number')
        parser.rule('data','data')

- define and execute statement

        statement = "(x1 & x2);"
        output = parser(statement, memory)

__OUTPUT:__ *True*
