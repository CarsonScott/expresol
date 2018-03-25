# expresol

Expresol is an easy-to-use python library for creating, parsing and executing statements in a user-defined language. The expresol library contains two main parts, namely the memory class and the parser class, which collectively work as a system of information that is accessed and manipulated through statements, where each statement is converted into hierarchical sets of instructions and then  executed recursively until the top-level instruction produces an output. 

---

__EXAMPLE CODE__:

- import library and create memory with 10 elements
        
        from expresol import *tha
        memory = Memory(10)

- store functions, data, and syntax markers in memory  

        memory.var(0, Marker('open'))
        memory.var(1, Marker('close'))
        memory.var(2, Marker('end'))
        memory.var(3, AND)
        memory.var(4, True)
        memory.var(5, True)

- assign symbols to elements that allow data to be accessed when observed in a statement 

        memory.ref(0, '(', 'grammar')
        memory.ref(1, ')', 'grammar')
        memory.ref(2, ';', 'grammar')
        memory.ref(3, '&', 'operator')
        memory.ref(4, 'x1', 'data')
        memory.ref(5, 'x2', 'data')

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
