from exercise_11 import getHoursMinutesSeconds


def test_1():
    assert getHoursMinutesSeconds(30) == "30s"


def test_2():
    assert getHoursMinutesSeconds(60) == "1m"


def test_3():
    assert getHoursMinutesSeconds(90) == "1m 30s"


def test_4():
    assert getHoursMinutesSeconds(3600) == "1h"


def test_5():
    assert getHoursMinutesSeconds(3601) == "1h 1s"


def test_6():
    assert getHoursMinutesSeconds(3661) == "1h 1m 1s"


def test_7():
    assert getHoursMinutesSeconds(90042) == "25h 42s"


def test_8():
    assert getHoursMinutesSeconds(0) == "0s"