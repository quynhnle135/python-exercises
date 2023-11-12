from exercise_9 import getChessSquareColor


def test_1():
    assert getChessSquareColor(1, 1) == "white"


def test_2():
    assert getChessSquareColor(2, 1) == "black"


def test_3():
    assert getChessSquareColor(1, 2) == "black"


def test_4():
    assert getChessSquareColor(8, 8) == "white"


def test_5():
    assert getChessSquareColor(0, 8) == ""


def test_6():
    assert getChessSquareColor(2, 9) == ""