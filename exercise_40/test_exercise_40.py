from exercise_40 import mergeTwoLists


def test_1():
    assert mergeTwoLists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9]


def test_2():
    assert mergeTwoLists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]


def test_3():
    assert mergeTwoLists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]


def test_4():
    assert mergeTwoLists([1, 2, 3], []) == [1, 2, 3]