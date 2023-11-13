from exercise_42 import bubbleSort


def test_1():
    assert bubbleSort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4]


def test_2():
    assert bubbleSort([2, 2, 2, 2]) == [2, 2, 2, 2]