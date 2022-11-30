# Keywords and symbols
# https://lojban.org/publications/reference_grammar/chapter18.html
numbers = ['pa', 're', 'ci', 'vo', 'mu', 'xa', 'ze', 'bi', 'so', 'no']
operations = ["su'i", "vu'u", "pi'i", "division"]
# me'i is less than, za'u is more than, du is equal, na'ebo is not equal
logical_operations = ["me'i", "za'u", "du", "na'ebo"]
words = ["\n", "bai"]  # bai is if
symbols = ","
keywords = numbers + operations + logical_operations + words


# Purpose of a lexer is to send tokens (words) to the parser
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


def lexer(sentence_array):
    if len(sentence_array[-1]) == 0:
        sentence_array.pop()

    array = []
    for word in sentence_array:
        if contains(word, numbers):
            array.append("digit")
        elif contains(word, operations):
            array.append("op")
        elif word == "du":
            array.append("equal")
        elif word == "bai":
            array.append("if")
        elif word == ",":
            array.append(",")
        elif contains(word, logical_operations):
            array.append("logic_op")
        else:
            if len(word) > 0:
                array.append("var")

    return array


def contains(item, array):
    for x in array:
        if x == item:
            return True
    return False

