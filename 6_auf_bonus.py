from utils import *

# Das Eingeben eines Statements ist nicht sehr ergonomisch momentan, deshalb ist unten die Funktion "parse_statement_from_string" implementiert.
# Schaue dir die Funktion an und versuche zu verstehen, wie sie funktioniert.
# Schreibe Kommentare im Code um zu erklären, was die Funktion macht.


class Num:
    def __init__(self, value):
        self.value = value

    def to_string(self):
        return str(self.value)

    def calculate(self):
        return self.value


class Statement:
    def __init__(self, left, operation, right):
        self.left = left
        self.operation = operation
        self.right = right

    def to_string(self):
        return "(" + self.left.to_string() + " " + self.operation + " " + self.right.to_string() + ")"

    def calculate(self):
        calculated_left = self.left.calculate()
        calculated_right = self.right.calculate()

        if self.operation == "+":
            return calculated_left + calculated_right
        elif self.operation == "-":
            return calculated_left - calculated_right
        elif self.operation == "*":
            return calculated_left * calculated_right
        elif self.operation == "/":
            return calculated_left / calculated_right


# splits statement "(12 + 3)" into tokens ["(", 12, "+", 3, ")"]
def tokenize_statement(statement):
    tokens = []

    lastNumber = ""

    for character in statement:
        characterIsDigit = character.isdigit()

        # Number token has finished parsing add it tokens
        if not characterIsDigit and lastNumber != "":
            tokens.append(int(lastNumber))
            lastNumber = ""

        if characterIsDigit:
            lastNumber += character  # append digit to lastNumber
        elif character == " ":
            continue
            # skips whitespace
        elif character in ["(", ")", "+", "-", "*", "/"]:
            tokens.append(character)
        else:
            raise Exception("Invalid character in statement: " + character)

    return tokens


# these are some test cases if tokenize_statement works as expected
assert tokenize_statement("(12 + 3)") == ["(", 12, "+", 3, ")"]
assert tokenize_statement("( 12   - 3)") == ["(", 12, "-", 3, ")"]
assert tokenize_statement("( 12   - 3 *(23+1))") == ["(", 12, "-", 3, "*", "(", 23, "+", 1, ")", ")"]


def parse_statement(tokens):
    token = tokens.pop(0)  # get first token from list
    if token == "(":
        left = parse_statement(tokens)
        operation = tokens.pop(0)
        assert operation in ["+", "-", "*", "/"], "Expected operation, but got " + operation
        right = parse_statement(tokens)
        closing_bracket = tokens.pop(0)
        assert closing_bracket == ")", "Expected closing bracket, but got " + closing_bracket

        return Statement(left, operation, right)

    elif isinstance(token, int):  # check if token is a number
        return Num(token)

    else:
        raise Exception("Expected statement or number instead got: " + token)


def parse_statement_from_string(statement):
    return parse_statement(tokenize_statement(statement))


print(parse_statement_from_string("(12 + 3)").calculate())  # 15
print(parse_statement_from_string("((12 * 3) + (4 / 2))").calculate())  # 40


# Zusätzlich (nicht Aufgabe 6) #########################################################################
# Mit dieser Funktion lässt sich eine Konsolen Rechner erstellen:
def console_calculator():
    while True:
        try:
            statement = input("Enter a statement: ")
            print(parse_statement_from_string(statement).calculate())
        except Exception as e:
            print("Error: " + str(e))


# Uncomment to try the console calculator
console_calculator()
