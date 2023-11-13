from exercise_35 import getTitleCase


def test_1():
    assert getTitleCase("Hello, world!") == "Hello, World!"


def test_2():
    assert getTitleCase("HELLO") == "Hello"


def test_3():
    assert getTitleCase("hElLo") == "Hello"


def test_4():
    assert getTitleCase("") == ""


def test_5():
    assert getTitleCase("abc123xyz") == "Abc123Xyz"


def test_6():
    assert getTitleCase("cat dog rat") == "Cat Dog Rat"


def test_7():
    assert getTitleCase("cat, dog, rat") == "Cat, Dog, Rat"