from exercise_33 import commaFormat


def test_1():
    assert commaFormat(1) == "1"


def test_2():
    assert commaFormat(10) == "10"


def test_3():
    assert commaFormat(100) == "100"


def test_4():
    assert commaFormat(1000) == "1,000"


def test_5():
    assert commaFormat(10000) == "10,000"


def test_6():
    assert commaFormat(1234567890) == "1,234,567,890"


def test_7():
    assert commaFormat(1000.123456) == "1,000.123456"