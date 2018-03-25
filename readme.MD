# expresol

An easy-to-use python library for creating, translating and executing statements in a user-defined language. The expresol library contains two main parts, namely the memory and the parser. Each contributes differently to the process of translating and then executing the instructions given by a statement.

---

__EXAMPLE CODE__:

- import expresol library
        
        from expresol import Memory, Parser, AND

- create memory with 10 elements

        memory = Memory(10)

- store functions, data structures, and syntax information in memory  

        memory.dat(0, True)
        memory.dat(1, True)
        
        memory.dat(2, AND)

        memory.dat(3, 'open')
        memory.dat(4, 'close')
        memory.dat(5, 'end')

- assign symbols to elements that allow their data to be accessed when observed in a statement 

        memory.var('a', 0, 'data')
        memory.var('b', 1, 'data')
        
        memory.var('&', 2, 'operator')
 
        memory.var('(', 3, 'grammar')
        memory.var(')', 4, 'grammar')
        memory.var(';', 5, 'grammar')

- create parser with 4-classes of symbols

        parser = Parser(['grammar', 'data', 'operator', 'number'])

- store valid sets of characters for each class

        parser.type('grammar','();')
        parser.type('number','1234567890')
        parser.type('operator','&|!+-*/=')
        parser.type('data','abcdefghijklmnopqrstuvwxyz')

- store pairs of classes that are valid when observed consequetively in a given statement

        parser.rule('operator','operator')
        parser.rule('grammar','none')
        parser.rule('none','grammar')
        parser.rule('data','number')
        parser.rule('data','data')

- execute statement

        statement = '(a & b);'
        output = parser(statement, memory)
        
*output: True*
