from exercise_15 import findMedian


def test_1():
    assert findMedian([]) == None


def test_2():
    assert findMedian([1, 2, 3]) == 2


def test_3():
    assert findMedian([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5


def test_4():
    assert findMedian([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6