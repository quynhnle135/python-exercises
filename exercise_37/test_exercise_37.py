from exercise_37 import makeChange

def test_1():
    assert makeChange(30) == {'quarters': 1, 'nickles': 1}


def test_2():
    assert makeChange(10) == {'dimes': 1}


def test_3():
    assert makeChange(57) == {'quarters': 2, 'nickles': 1, 'pennies': 2}


def test_4():
    assert makeChange(100) == {'quarters': 4}


def test_5():
    assert makeChange(125) == {'quarters': 5}