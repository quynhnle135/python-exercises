from exercise_31 import convertIntToStr


def test_1():
    for i in range(-10000, 10000):
        assert convertIntToStr(i) == str(i)