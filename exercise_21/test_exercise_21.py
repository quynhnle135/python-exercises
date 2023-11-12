from exercise_21 import isValidDate


def test_1():
    assert isValidDate(1999, 12, 31) == True


def test_2():
    assert isValidDate(2000, 2, 29) == True


def test_3():
    assert isValidDate(2029, 13, 1) == False


def test_4():
    assert isValidDate(10000000, 1, 1) == True


def test_5():
    assert isValidDate(2015, 4, 31) == False


def test_6():
    assert isValidDate(1970, 5, 99) == False


def test_7():
    assert isValidDate(1981, 0, 3) == False


def test_8():
    assert isValidDate(1666, 4, 0) == False