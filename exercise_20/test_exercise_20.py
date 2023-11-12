from exercise_20 import isLeapYear


def test_1():
    assert isLeapYear(1999) == False


def test_2():
    assert isLeapYear(2000) == True


def test_3():
    assert isLeapYear(2001) == False


def test_4():
    assert isLeapYear(2004) == True


def test_5():
    assert isLeapYear(2100) == False


def test_6():
    assert isLeapYear(2400) == True