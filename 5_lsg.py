from utils import *

# Wir führen eine weitere Methode calculate ein, die soll das Statement berechnen und den Wert zurückgeben.
# Dafür ist ist einiges schon vorbereitet, füge bei den TODOs den fehlenden Code ein.
# Folgende Operationen sollen unterstützt werden: +, -, *, /


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


check_5(Statement(Num(1), "+", Num(2)), 3)
check_5(Statement(Num(1), "+", Statement(Num(2), "*", Num(3))), 7)
check_5(Statement(Statement(Num(2), "+", Num(3)), "*", Num(2)), 10)
check_5(Statement(Statement(Num(2), "*", Num(3)), "/", Num(2)), 3)
