from exercise_4 import findArea, findPerimeter, findVolume, findSurfaceArea
import pytest


def test_1():
    assert findArea(10, 10) == 100


def test_2():
    assert findArea(0, 9999) == 0


def test_3():
    assert findArea(5, 8) == 40


def test_4():
    assert findPerimeter(10, 10) == 40


def test_5():
    assert findPerimeter(0, 9999) == 19998


def test_6():
    assert findPerimeter(5, 8) == 26


def test_7():
    assert findVolume(10, 10, 10) == 1000


def test_8():
    assert findVolume(9999, 0, 9999) == 0


def test_9():
    assert findVolume(5, 8, 10) == 400


def test_10():
    assert findSurfaceArea(10, 10, 10) == 600


def test_11():
    assert findSurfaceArea(9999, 0, 9999) == 199960002


def test_12():
    assert findSurfaceArea(5, 8, 10) == 340


def test_13():
    with pytest.raises(ValueError):
        findArea(-5, -1)


def test_14():
    with pytest.raises(ValueError):
        findPerimeter(-5, -1)


def test_15():
    with pytest.raises(ValueError):
        findVolume(-5, -5, -5)


def test_16():
    with pytest.raises(ValueError):
        findSurfaceArea(-10, -10, -10)