import lojban_compiler
import lojban_parser
from lojban_lexer import *
from lojban_parser import parser


def main():
    file = open("test-class.txt", "r")
    string = file.read()

    array = scanner(string)
    array2d_words = line_divider(array)

    for statement in array2d_words:
        array_tokens = lexer(statement)
        parser(array_tokens)
        print("")

    if lojban_parser.has_error:
        print("Input Error: Stopping Compling")
        return 1
    else:
        print("\n\nCompiling...")

    for statement in array2d_words:
        array_tokens = lexer(statement)
        lojban_compiler.compiler(array_tokens, statement)

    print("Done!")


main()
