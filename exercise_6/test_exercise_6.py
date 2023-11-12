from exercise_6 import ordinal_suffix, ordinalSuffix


def test_1():
    assert ordinalSuffix(1) == "1st"


def test_2():
    assert ordinalSuffix(2) == "2nd"


def test_3():
    assert ordinalSuffix(3) == "3rd"


def test_4():
    assert ordinalSuffix(4) == "4th"


def test_5():
    assert ordinalSuffix(10) == "10th"


def test_6():
    assert ordinalSuffix(11) == "11th"


def test_7():
    assert ordinalSuffix(12) == "12th"


def test_8():
    assert ordinalSuffix(13) == "13th"


def test_9():
    assert ordinalSuffix(14) == "14th"


def test_10():
    assert ordinalSuffix(101) == "101st"


def test_11():
    assert ordinalSuffix(115) == "115th"


def test_12():
    assert ordinalSuffix(121) == "121st"


def test_13():
    assert ordinalSuffix(111) == "111th"


def test_14():
    assert ordinalSuffix(112) == "112th"


def test_15():
    assert ordinalSuffix(113) == "113th"


def test_16():
    assert ordinalSuffix(120) == "120th"


def test_17():
    assert ordinal_suffix(1) == "1st"


def test_18():
    assert ordinal_suffix(2) == "2nd"


def test_19():
    assert ordinal_suffix(3) == "3rd"


def test_20():
    assert ordinal_suffix(4) == "4th"


def test_21():
    assert ordinal_suffix(10) == "10th"


def test_22():
    assert ordinal_suffix(11) == "11th"


def test_23():
    assert ordinal_suffix(12) == "12th"


def test_24():
    assert ordinal_suffix(13) == "13th"


def test_25():
    assert ordinal_suffix(14) == "14th"


def test_26():
    assert ordinal_suffix(101) == "101st"


def test_27():
    assert ordinal_suffix(115) == "115th"


def test_28():
    assert ordinal_suffix(121) == "121st"


def test_29():
    assert ordinal_suffix(111) == "111th"


def test_30():
    assert ordinal_suffix(112) == "112th"


def test_31():
    assert ordinal_suffix(113) == "113th"


def test_32():
    assert ordinal_suffix(120) == "120th"