from exercise_41 import rot13


def test_1():
    assert rot13("Hello, world!") == "Uryyb, jbeyq!"


def test_2():
    assert rot13("Uryyb, jbeyq!") == "Hello, world!"


def test_3():
    assert rot13(rot13("Hello, world!")) == "Hello, world!"


def test_4():
    assert rot13("abcdefghijklmnopqrstuvwxyz") == "nopqrstuvwxyzabcdefghijklm"