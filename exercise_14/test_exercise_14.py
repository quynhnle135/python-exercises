from exercise_14 import findAverage


def test_1():
    assert findAverage([1, 2, 3]) == 2


def test_2():
    assert findAverage([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2


def test_3():
    assert findAverage([12, 20, 37]) == 23


def test_4():
    assert findAverage([0, 0, 0, 0, 0]) == 0