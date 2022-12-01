import lojban_compiler
from lojban_lexer import *
from lojban_parser import parser


def main():
    file = open("test-class.txt", "r")
    string = file.read()

    array = scanner(string)
    array2d_words = line_divider(array)

    # Removes comments
    for statement in array2d_words:
        if len(statement) == 0:
            continue
        if statement[0] == "#":
            array2d_words.remove(statement)

    for statement in array2d_words:
        if len(statement) == 0:
            array2d_words.remove(statement)

    for statement in array2d_words:
        array_tokens = lexer(statement)
        parser(array_tokens)
        print("")



    print("Compiling...")

    for statement in array2d_words:
        array_tokens = lexer(statement)
        lojban_compiler.compiler(array_tokens, statement)

    print("Done!")


main()
