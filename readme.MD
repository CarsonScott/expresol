# expresol

An easy-to-use python library for creating, translating and executing statements in a user-defined language. The expresol library contains two main parts, namely the memory and the parser. Each contributes differently to the process of translating and then executing the instructions given by a statement.

---

__EXAMPLE CODE__:

- import expresol library
        
        from expresol import Memory, Parser, AND

- create memory with 10 elements

        memory = Memory(10)

- store functions, data structures, and syntax information in memory  

        emory.set_data(0, True)
        memory.set_data(1, True)
        
        memory.set_data(2, AND)

        memory.set_data(3, 'open')
        memory.set_data(4, 'close')
        memory.set_data(5, 'end')

- assign symbols to elements that allow their data to be accessed when observed in a statement 

        memory.set_variable('a', 0, 'data')
        memory.set_variable('b', 1, 'data')
        
        memory.set_variable('&', 2, 'operator')
 
        memory.set_variable('(', 3, 'grammar')
        memory.set_variable(')', 4, 'grammar')
        memory.set_variable(';', 5, 'grammar')

- create parser with 4-classes of symbols

        parser = Parser(['grammar', 'data', 'operator', 'number'])

- store valid sets of characters for each class

        parser.add_type('grammar','();')
        parser.add_type('number','1234567890')
        parser.add_type('operator','&|!+-*/=')
        parser.add_type('data','abcdefghijklmnopqrstuvwxyz')

- store pairs of classes that are valid when observed consequetively in a given statement

        parser.add_rule(('operator','operator'))
        parser.add_rule(('grammar','none'))
        parser.add_rule(('none','grammar'))
        parser.add_rule(('data','number'))
        parser.add_rule(('data','data'))

- execute statement

        statement = '(a & b);'
        output = parser(statement, memory)
        
*output: True*
