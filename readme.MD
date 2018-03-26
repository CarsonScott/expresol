# expresol

Expresol is an easy-to-use ibrary for executing customizable script-languages in python. The expresol library contains two main components, the memory and the parser, which collectively work as an information system whose data is accessible via statements that manipulate stored variables when executed. Each statement is converted to an executable form containing hierarchical sets of operators and data. Each set contains a set of elements, corresponding to either variables or operators. The most common possible structure of a valid statement is as folliows: 

    (a + b)

containing three elements, 'a', '+' and 'b', where middle element denotes an operator and the rest denote variables. The second possible structure is:

    (~ a)

containing two elements, '~" and 'a', where The left symbol denotes an operator and the right denotes a variable. The last possible structure is:

    (a)

in which there is one element, 'a', where the symbol denotes a variable. The identity function is assigned by default if no operator is present, meaning the output of this statement simply returns the value of 'a'. 

---

__EXAMPLE CODE__:

- import library and create memory with 10 elements
        
        from expresol import *
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
