from exercise_17 import rollDice


def test_1():
    assert 1 <= rollDice(1) <= 6


def test_2():
    assert 2 <= rollDice(2) <= 12


def test_3():
    assert 3 <= rollDice(3) <= 18