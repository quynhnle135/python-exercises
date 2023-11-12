from exercise_16 import findMode


def test_1():
    assert findMode([]) == None


def test_2():
    assert findMode([1, 2, 3, 4, 4]) == 4


def test_3():
    assert findMode([1, 1, 2, 3, 4]) == 1