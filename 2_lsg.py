from utils import *

# Erstelle eine Methode to_string auf der Klasse Statement, die das Statement als String (z.B. "(1 + 2)")) zurückgibt.


class Statement:
    def __init__(self, left, operation, right):
        self.left = left
        self.operation = operation
        self.right = right

    def to_string(self):
        return "(" + str(self.left) + " " + self.operation + " " + str(self.right) + ")"


check_2(Statement(1, "+", 2).to_string())
