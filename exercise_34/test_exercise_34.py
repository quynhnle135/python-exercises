from exercise_34 import getUpperCase


def test_1():
    assert getUpperCase("Hello") == "HELLO"


def test_2():
    assert getUpperCase("hello") == "HELLO"


def test_3():
    assert getUpperCase("HELLO") == "HELLO"


def test_4():
    assert getUpperCase("Hello, world!") == "HELLO, WORLD!"


def test_5():
    assert getUpperCase("Goodbye 123") == "GOODBYE 123"


def test_6():
    assert getUpperCase("12345") == "12345"


def test_7():
    assert getUpperCase("") == ""