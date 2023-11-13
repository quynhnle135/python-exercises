from exercise_39 import collatz


def test_1():
    assert collatz(0) == []


def test_2():
    assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]


def test_3():
    assert collatz(11) == [11, 34, 17, 52, 26, 13, 40, 20 , 10, 5, 16, 8, 4, 2, 1]