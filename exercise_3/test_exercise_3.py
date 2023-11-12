from exercise_3 import isEven, isOdd


def test_1():
    assert isOdd(42) == False


def test_2():
    assert isOdd(9999) == True


def test_3():
    assert isOdd(-10) == False


def test_4():
    assert isOdd(-11) == True


def test_5():
    assert isOdd(3.1415) == False


def test_6():
    assert isEven(42) == True


def test_7():
    assert isEven(9999) == False


def test_8():
    assert isEven(-10) == True


def test_9():
    assert isEven(-11) == False


def test_10():
    assert isEven(3.1415) == False