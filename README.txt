Lojban Compiler

1. Feed a text document with commands to main.py. (default = "test-class.txt")
2. Run main.py that invokes the lexer, parser, and interpreter.
3. Output will show in terminal.
	-First will show each statement (separated at new lines) being subject to the parser
	-If everything is grammatically correct, it will show "Compiling..." with print statements
	 showing outcomes of each statement's impact
		Ex. Set variable apple to 3
		Ex. Value of expression is 0.5



Grammar:
# statement:    <stmt> -> <expr> | <assignment> | <conditional> | <loop>
# loop:         <loop> -> ganfauke <number>:<number>, <assignment>
# conditional:  <conditional> -> if <logic>, <statement>
# logic expr:   <logic> -> <factor> (==, !=, >=, <=) <factor>
# assignment:   <assignment> -> <var> <equal> <expr>
# expression:   <expr> -> <factor> [(+ | - | * | /) factor]
# factor:       <factor> -> <num> | <expr> | <var>
# number:       <num> -> <digit> | <digit><num>
# digit:        <digit> -> 0 - 9


Includes:
-Allows comments starting with #
-Expression solving
	Includes addition, subtraction, multiplication, and divison	
-Variable assignment
	Variables can be used in expressions and assignments
-If statements
-Simple for loop



Information from https://lojban.org/publications/reference_grammar/chapter18.html


By Tessla Muir
https://github.com/tessla-muir
www.tessla-muir.com
11/30/2022