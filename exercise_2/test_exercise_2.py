from exercise_2 import convertToFahrenheit, convertToCelsius

def test_1():
    assert convertToCelsius(0) == -17.77777777777778


def test_2():
    assert convertToCelsius(180) == 82.22222222222223


def test_3():
    assert convertToFahrenheit(0) == 32.0


def test_4():
    assert convertToFahrenheit(100) == 212


def test_5():
    assert convertToCelsius(convertToFahrenheit(15)) == 15.0
