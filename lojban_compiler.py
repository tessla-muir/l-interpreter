import sys

global variable_names
variable_names = []
global variable_values
variable_values = []

global has_error
has_error = False

global token_sentence
global next_token

global lexeme_sentence
global next_lexeme

global index
index = 0

global var_count
var_count = 0


def compiler(sentence_tokens, sentence_lexemes):
    global token_sentence, lexeme_sentence, index
    lexeme_sentence = sentence_lexemes
    token_sentence = sentence_tokens
    lex()
    statement()

    # Reset values
    index = 0


# No precedence in Lojban
# statement:    <stmt> -> <expr> | <assignment> | <conditional>

# conditional:  <conditional> -> if <logic>, <statement>
# logic expr:   <logic> -> <factor> (==, !=, >=, <=) <factor>

# assignment:   <assignment> -> <var> <equal> <expr>
# expression:   <expr> -> <factor> [(+ | - | * | /) factor]
# factor:       <factor> -> <num> | <expr> | <var>
# number:       <num> -> <digit> | <digit><num>
# digit:        <digit> -> 0 - 9

def statement():
    if next_token == "var" and peek("equal"):
        assignment()
    elif next_token == "if":
        conditional()
    else:
        num = expression()
        print("Value of expression is " + str(num))


def conditional():
    # Pass by the if and comma
    lex()
    value = logic_expression()
    lex()
    print("The expression is " + str(value))

    if value:
        statement()


def logic_expression():
    value = False
    num1 = factor()

    if next_token == "logic_op" or next_token == "equal":
        op = next_lexeme
        lex()
        num2 = factor()
        value = logical_calculate(num1, num2, op)

    return value


def logical_calculate(num1, num2, op):
    if op == "du":
        return num1 == num2
    elif op == "na'ebo":
        return num1 != num2
    elif op == "me'i":
        return num1 < num2
    elif op == "za'u":
        return num1 > num2


def assignment():
    global var_count
    var = next_lexeme
    num = 0

    if next_token == "var":
        lex()
        lex()
        if next_token == "var" and peek("END"):
            return
        elif next_token == "var" and not peek("END"):
            num = expression()
        elif next_token == "digit":
            num = expression()

    variable_names.append(var)
    variable_values.append(num)
    print("Set variable " + variable_names[var_count] + " to " + str(variable_values[var_count]))
    var_count += 1


def expression():
    num1 = factor()

    while next_token == "op":
        op = next_lexeme
        lex()
        num2 = factor()
        num1 = calculate(num1, num2, op)

    return num1


def calculate(num1, num2, op):
    # Calculate
    if op == "su'i":
        num1 += num2
    elif op == "vu'u":
        num1 -= num2
    elif op == "pi'i":
        num1 *= num2
    elif op == "division":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
            sys.exit(1)
        num1 /= num2

    return num1


def factor():
    if next_token == "digit":
        num = number()
        return num
    elif next_token == "var":
        i = find_index(next_lexeme)
        if i == -1:
            print("Variable not found!")
            sys.exit(1)
        lex()
        return variable_values[i]


def find_index(var_name):
    i = 0
    for value in variable_names:
        if value == var_name:
            return i
        i += 1
    return -1


def number():
    value = 0
    if next_token == "digit":
        while next_token == "digit":
            value *= 10
            value += digit(lexeme_sentence[index-1])
            lex()
    return value


def digit(word):
    if word == "pa":
        return 1
    elif word == "re":
        return 2
    elif word == "ci":
        return 3
    elif word == "vo":
        return 4
    elif word == "mu":
        return 5
    elif word == "xa":
        return 6
    elif word == "ze":
        return 7
    elif word == "bi":
        return 8
    elif word == "so":
        return 9
    elif word == "no":
        return 0


def peek(token):
    if index < len(token_sentence) and token_sentence[index] == token:
        return True
    else:
        return False


def error():
    global has_error
    has_error = True


# Sets next_token, increases index
def lex():
    global next_token, next_lexeme, index
    if len(token_sentence) > index:
        next_token = token_sentence[index]
        next_lexeme = lexeme_sentence[index]
        index += 1
    else:
        next_token = "END"
    # print("Next lexeme: " + next_lexeme)
