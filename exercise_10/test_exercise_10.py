from exercise_10 import findAndReplace


def test_1():
    assert findAndReplace("The fox", "fox", "dog") == "The dog"


def test_2():
    assert findAndReplace("fox", "fox", "dog") == "dog"


def test_3():
    assert findAndReplace("Firefox", "fox", "dog") == "Firedog"


def test_4():
    assert findAndReplace("foxfox", "fox", "dog") == "dogdog"


def test_5():
    assert findAndReplace("The Fox and the fox.", "fox", "dog") == "The Fox and the dog."