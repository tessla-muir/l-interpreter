# Keywords and symbols
# https://lojban.org/publications/reference_grammar/chapter18.html
numbers = ['pa', 're', 'ci', 'vo', 'mu', 'xa', 'ze', 'bi', 'so', 'no']
operations = ["su'i", "vu'u", "pi'i", "fe'i"]
# me'i is less than, za'u is more than, du is equal, na'ebo is not equal
logical_operations = ["me'i", "za'u", "du", "na'ebo"]
words = ["\n", "bai", "ganfauke"]  # bai is if, ganfauke is for while loops
symbols = [",", ":"]
keywords = numbers + operations + logical_operations + words + symbols


# Purpose of a lexer is to send tokens (words) to the parser
def lexer(sentence_array):
    array = []
    for word in sentence_array:
        if word in numbers:
            array.append("digit")
        elif word in operations:
            array.append("op")
        elif word == "du":
            array.append("equal")
        elif word == "bai":
            array.append("if")
        elif word == ",":
            array.append(",")
        elif word == ":":
            array.append(":")
        elif word in logical_operations:
            array.append("logic_op")
        elif word == "ganfauke":
            array.append("loop")
        else:
            if len(word) > 0:
                array.append("var")

    return array


def scanner(string):
    array = []
    word = ""
    index = 0
    for char in string:
        if char != " ":
            word += char

        if index + 1 < len(string):
            # If next character is a space, or it's a keyword...
            if string[index+1] == " " or string[index+1] in keywords or word in keywords:
                if word != "":
                    array.append(word.replace('\n', '<new line>'))
                    word = ""
        index += 1

    array.append(word)
    return array


def line_divider(long_array):
    array = []
    array2d = []

    for word in long_array:
        # Add word to array if not a new line
        if word != "<new line>":
            array.append(word)
        # At new lines, add sentence to 2D array
        else:
            array2d.append(array)
            array = []

    array2d.append(array)
    array = []
    return array2d

