from t3_oefeningen_2 import (
    Cirkel,
    is_even,
    is_oneven,
    is_palindroom,
    pythagoras,
    stats,
    volume_bol,
    volume_donut,
)


def test_is_even_1():
    result = is_even(1)
    assert result is False


def test_is_even_2():
    result = is_even(2)
    assert result is True


def test_is_even_3():
    result = is_even(3)
    assert result is False


def test_is_oneven_1():
    result = is_oneven(1)
    assert result is True


def test_is_oneven_2():
    result = is_oneven(2)
    assert result is False


def test_is_oneven_3():
    result = is_oneven(3)
    assert result is True


def test_volume_bol_straal_1():
    result = volume_bol(1)
    assert abs(result - 4.1) < 0.1


def test_volume_bol_straal_16():
    result = volume_bol(16)
    assert abs(result - 17157.2) < 0.1


def test_volume_donut_3_7():
    result = volume_donut(r=3, R=7)
    expected = 1243.57
    assert abs(result - expected) < 0.1


def test_volume_donut_2_4():
    result = volume_donut(r=2, R=4)
    expected = 315.83
    assert abs(result - expected) < 0.1


def test_volume_donut_4_4():
    result = volume_donut(r=4, R=4)
    expected = -1
    assert result == expected


def test_stats_1():
    punten = [5]
    result = stats(punten)
    assert result == [5.0, 5, 5, 1]


def test_stats_4():
    punten = [5, 9, 10, 8]
    result = stats(punten)
    assert abs(result[0] - 8.0) < 0.1
    assert result[1:] == [10, 5, 4]


def test_stats_6():
    punten = [5, 0, 9.5, 8, 6, 7]
    gemiddelde, maximum, minimum, nr = stats(punten)
    assert abs(gemiddelde - 5.9) < 0.1
    assert minimum == 0
    assert maximum == 9.5
    assert nr == 6


def test_cirkel_straal_4_omtrek():
    x = Cirkel(4)
    assert abs(x.omtrek() - 25.13) < 0.1


def test_cirkel_straal_4_oppervlakte():
    x = Cirkel(4)
    assert abs(x.oppervlakte() - 50.27) < 0.1


def test_cirkel_straal_4_str():
    x = Cirkel(4)
    assert f"{x}" == "cirkel met straal 4"


def test_cirkel_straal_5_omtrek():
    x = Cirkel(5)
    assert abs(x.omtrek() - 31.42) < 0.1


def test_cirkel_straal_5_oppervlakte():
    x = Cirkel(5)
    assert abs(x.oppervlakte() - 78.54) < 0.1


def test_cirkel_straal_5_str():
    x = Cirkel(5)
    assert f"{x}" == "cirkel met straal 5"


def test_pythagoros_1():
    result = pythagoras(a=1, b=1)
    expected = 1.41

    assert abs(result - expected) < 0.1


def test_pythagoros_2():
    result = pythagoras(a=2, b=2)
    expected = 2.83

    assert abs(result - expected) < 0.1


def test_pythagoros_4_5():
    result = pythagoras(a=4, b=5)
    expected = 6.4

    assert abs(result - expected) < 0.1


def test_pythagoros_01_03():
    result = pythagoras(a=0.1, b=0.3)
    expected = 0.32

    assert abs(result - expected) < 0.1


def test_pythagoros_a_neg():
    result = pythagoras(a=-1, b=3)
    expected = -1

    assert result == expected


def test_pythagoros_b_neg():
    result = pythagoras(a=1, b=-4)
    expected = -1

    assert result == expected


def test_pythagoros_ab_neg():
    result = pythagoras(a=-2, b=-3)
    expected = -1

    assert result == expected


def test_is_palindroom():
    result = is_palindroom("anna")
    assert result is True


def test_is_geen_palindroom():
    result = is_palindroom("konijn")
    assert result is False