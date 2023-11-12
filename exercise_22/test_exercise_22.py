from exercise_22 import rpsWinner


def test_1():
    assert rpsWinner("rock", "paper") == "player 2"


def test_2():
    assert rpsWinner("rock", "scissors") == "player 1"


def test_3():
    assert rpsWinner("paper", "scissors") == "player 2"


def test_4():
    assert rpsWinner("paper", "rock") == "player 1"


def test_5():
    assert rpsWinner("scissors", "rock") == "player 2"


def test_6():
    assert rpsWinner("scissors", "paper") == "player 1"


def test_7():
    assert rpsWinner("rock", "rock") == "tie"