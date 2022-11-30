import sys

global token_sentence
global next_token
global index
index = 0


def parser(new_sentence):
    print("Parsing!")
    global token_sentence, next_token, index
    token_sentence = new_sentence
    lex()
    statement()

    if next_token != "END":
        print("Interpret error: Expected no other tokens!")
        error()
        return

    # Reset values
    index = 0


# No precedence in Lojban
# statement:    <stmt> -> <expr> | <assignment> | <conditional>

# conditional:  <conditional> -> if <logic_expr>, ( <logic> | <assignment> )
# logic expr:   <logic> -> <factor> (==, !=, >=, <=) <factor>

# assignment:   <assignment> -> <var> <equal> <expr>
# expression:   <expr> -> <factor> [(+ | - | * | /) factor]
# factor:       <factor> -> <num> | <expr> | <var>
# number:       <num> -> <digit> | <digit><num>
# digit:        <digit> -> 0 - 9


def statement():
    print("Enter <statement>")

    if next_token == "var" and peek("equal"):
        assignment()
    elif next_token == "if":
        conditional()
    else:
        expression()

    print("Exit <statement>")


def conditional():
    # Pass by the if
    lex()
    if next_token == ",":
        lex()
        logic_expression()
    else:
        print("Conditional error: missing comma")
        error()


def logic_expression():
    print("Enter <logic>")

    factor()

    if next_token == "logic_op":
        lex()
        factor()
    else:
        print("Logic error: Not valid expression")
        error()

    print("Exit <logic>")


def assignment():
    print("Enter <assignment>")

    if next_token == "var" and peek("equal"):
        lex()
        lex()
        if next_token == "var" and peek("END"):
            return
        elif next_token == "var" and not peek("END"):
            expression()
        elif next_token == "digit":
            expression()
        else:
            print("Assignment error: Not valid assignment")
            error()
    else:
        print("Assignment error: Not valid assignment")
        error()

    print("Exit <assignment>")


def expression():
    print("Enter <expr>")

    factor()

    while next_token == "op":
        lex()
        factor()

    print("Exit <expr>")


def factor():
    print("Enter <factor>")

    if next_token == "digit":
        number()
    elif next_token == "var":
        lex()
    else:
        print("Factor error: Not a number or expression")
        error()

    print("Exit <factor>")


def number():
    print("Enter <num>")

    if next_token == "digit":
        while next_token == "digit":
            lex()
    else:
        print("Number error: No digits in passed input")
        error()

    print("Exit <num>")


def peek(token):
    if index < len(token_sentence) and token_sentence[index] == token:
        return True
    else:
        return False


def error():
    sys.exit(1)


# Sets next_token, increases index
def lex():
    global next_token, index
    if len(token_sentence) > index:
        next_token = token_sentence[index]
        index += 1
    else:
        next_token = "END"
    print("Next token: " + next_token)
