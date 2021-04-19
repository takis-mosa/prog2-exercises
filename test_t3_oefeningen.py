from t3_oefeningen import (
    bmi,
    omtrek_cirkel,
    oppervlakte_cirkel,
    oppervlakte_vierkant,
    volume_cilinder,
    volume_kubus,
)


def test_oppervlakte_vierkant():
    resultaat = oppervlakte_vierkant(zijde=2)
    assert resultaat == 4


def test_volume_kubus():
    resultaat = volume_kubus(zijde=2)
    assert resultaat == 8


def test_volume_kubus_negatieve_zijde():
    resultaat = volume_kubus(zijde=-3)
    assert resultaat == 0


def test_omtrek_cirkel():
    resultaat = omtrek_cirkel(r=4)
    assert abs(resultaat - 25.13) < 0.1


def test_oppervlakte_cirkel():
    resultaat = oppervlakte_cirkel(r=2)
    assert abs(resultaat - 12.56) < 0.1


def test_volume_cilinder():
    resultaat = volume_cilinder(r=2, h=4)
    assert abs(resultaat - 50.26548) < 0.1


def test_bmi():
    resultaat = bmi(80, 1.835)
    assert abs(resultaat - 24) < 0.5


def test_bmi_ondergewicht():
    resultaat = bmi(50, 1.835)
    assert abs(resultaat - 14.8) < 0.5


def test_bmi_overgewicht():
    resultaat = bmi(90, 1.835)
    assert abs(resultaat - 26.7) < 0.5
