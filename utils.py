def TODO(message):
    raise NotImplementedError("Open TODO: " + message)


def check_1(statement):
    assert statement.left == 2, "Check failed: " + statement
    assert statement.operation == "+", "Check failed: " + statement
    assert statement.right == 3, "Check failed: " + statement
    print("Check passed")


def check_2(statement):
    assert statement == "(1 + 2)", "Check failed: " + statement
    print("Check passed")


def check_4(statement, expected):
    assert statement.to_string() == expected, f"Expected {expected}, but got {statement.to_string()}"
    print("Check passed")


def check_5(statement, expected):
    result = statement.calculate()
    assert result == expected, f"Expected {expected}, but got {result}"
    print("Check passed")
