from utils import *

# Für das weitere arbeiten, führen wir eine weitere Klasse "Num" ein, die eine Zahl repräsentiert.
# Diese Klasse soll die gleichen Methoden besitzen wie die Klasse Statement.


class Num:
    def __init__(self, value):
        self.value = value

    def to_string(self):
        return str(self.value)


# Reimplementiere Methode to_string auf der Klasse Statement, mit der Änderung, dass die Zahlen (in left & right) nun mit der Klasse Number repräsentiert werden.
# Verwende dafür einen Rekursiven Aufruf: damit wir des möglich auch verschachtelte Statements zu verwenden.


class Statement:
    def __init__(self, left, operation, right):
        self.left = left
        self.operation = operation
        self.right = right

    def to_string(self):
        TODO("Rekursiver Aufruf")


check_4(Statement(Num(1), "+", Num(2)), "(1 + 2)")
check_4(Statement(Num(1), "+", Statement(Num(2), "*", Num(3))), "(1 + (2 * 3))")
check_4(Statement(Statement(Num(2), "+", Num(3)), "*", Num(1)), "((2 + 3) * 1)")
