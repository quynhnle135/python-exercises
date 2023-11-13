from exercise_36 import reverseString, reverse_string, reverse_string_mirror_idx


def test_1():
    assert reverseString("Hello") == "olleH"


def test_2():
    assert reverse_string("Hello") == "olleH"


def test_3():
    assert reverse_string_mirror_idx("Hello") == "olleH"
