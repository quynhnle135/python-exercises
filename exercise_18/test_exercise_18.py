from exercise_18 import getCostOfCoffee


def test_1():
    assert getCostOfCoffee(7, 2.50) == 17.50


def test_2():
    assert getCostOfCoffee(8, 2.50) == 20


def test_3():
    assert getCostOfCoffee(9, 2.50) == 20.0


def test_4():
    assert getCostOfCoffee(10, 2.50) == 22.50


def test_5():
    for i in range(1, 4):
        assert getCostOfCoffee(0, 1) == 0
        assert getCostOfCoffee(8, i) == 8 * i
        assert getCostOfCoffee(9, i) == 8 * i
        assert getCostOfCoffee(18, i) == 16 * i
        assert getCostOfCoffee(19, i) == 17 * i
        assert getCostOfCoffee(30, i) == 27 * i