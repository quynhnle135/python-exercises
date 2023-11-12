from exercise_12 import getSmallest, getBiggest


def test_1():
    assert getSmallest([1, 2, 3]) == 1


def test_2():
    assert getBiggest([1, 2, 3]) == 3


def test_3():
    assert getSmallest([3, 2, 1]) == 1


def test_4():
    assert getBiggest([3, 2, 1]) == 3


def test_5():
    assert getSmallest([1]) == 1


def test_6():
    assert getBiggest([1]) == 1


def test_7():
    assert getSmallest([10, -20, 1, 3, 5, -100, -7, 28]) == -100


def test_8():
    assert getBiggest([10, -20, 1, 3, 5, -100, -7, 28]) == 28