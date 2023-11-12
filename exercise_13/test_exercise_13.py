from exercise_13 import calculateSum, calculateProduct


def test_1():
    assert calculateSum([]) == 0


def test_2():
    assert calculateSum([2, 4, 6, 8, 10]) == 30


def test_3():
    assert calculateProduct([]) == 1


def test_4():
    assert calculateProduct([2, 4, 6, 8, 10]) == 3840


def test_5():
    assert calculateSum([-2, -4, -6, -8, -10]) == -30


def test_6():
    assert calculateProduct([-2, -4, -6, -8, -10]) == -3840


def test_7():
    assert calculateProduct([1, 2, 3, 4, 5, 0]) == 0