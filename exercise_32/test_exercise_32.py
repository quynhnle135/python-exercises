from exercise_32 import convertStrToInt


def test_1():
    for i in range(-1000, 1000):
        assert convertStrToInt(str(i)) == i