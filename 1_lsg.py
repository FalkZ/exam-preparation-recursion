from utils import *

# Erstelle eine Klasse die folgendes räpresentiert: (2 + 3)
# Die Klasse soll Statement heissen.
#                                              (2        +            3)
# die Felder sollen folgend benennt werden:     ^ left   ^ operation  ^ right


class Statement:
    def __init__(self, left, operation, right):
        self.left = left
        self.operation = operation
        self.right = right


# Erstelle eine Instanz der Klasse die folgendes repräsentiert: (2 + 3)

check_1(Statement(2, "+", 3))
