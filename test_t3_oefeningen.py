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


def test_oppervlakte_vierkant_groot():
    resultaat = oppervlakte_vierkant(zijde=30)
    assert resultaat == 900


def test_oppervlakte_vierkant_negatieve_zijde():
    resultaat = oppervlakte_vierkant(zijde=-50)
    assert resultaat == -1


def test_volume_kubus():
    resultaat = volume_kubus(zijde=2)
    assert resultaat == 8


def test_volume_kubus_groot():
    resultaat = volume_kubus(zijde=20)
    assert resultaat == 8000


def test_volume_kubus_negatieve_zijde():
    resultaat = volume_kubus(zijde=-3)
    assert resultaat == 0


def test_omtrek_cirkel():
    resultaat = omtrek_cirkel(r=4)
    assert abs(resultaat - 25.13) < 0.1


def test_omtrek_cirkel_groot():
    resultaat = omtrek_cirkel(r=70)
    assert abs(resultaat - 439.8) < 0.1


def test_omtrek_cirkel_negatieve_straal():
    resultaat = omtrek_cirkel(r=-7)
    assert resultaat == -1


def test_oppervlakte_cirkel():
    resultaat = oppervlakte_cirkel(r=2)
    assert abs(resultaat - 12.56) < 0.1


def test_oppervlakte_cirkel_groot():
    resultaat = oppervlakte_cirkel(r=50)
    assert abs(resultaat - 7853.9) < 0.1


def test_oppervlakte_cirkel_negatieve_straal():
    resultaat = oppervlakte_cirkel(r=-2)
    assert resultaat == -1


def test_volume_cilinder():
    resultaat = volume_cilinder(r=2, h=4)
    assert abs(resultaat - 50.26548) < 0.1


def test_volume_cilinder_hoog():
    resultaat = volume_cilinder(r=3, h=100)
    assert abs(resultaat - 2827.43) < 0.1


def test_volume_cilinder_hoogte_negatief():
    resultaat = volume_cilinder(r=3, h=-1)
    assert resultaat == -1


def test_volume_cilinder_negatieve_straal():
    resultaat = volume_cilinder(r=-3, h=5)
    assert resultaat == -1


def test_bmi():
    resultaat = bmi(80, 1.835)
    assert abs(resultaat - 24) < 0.5


def test_bmi_ondergewicht():
    resultaat = bmi(50, 1.835)
    assert abs(resultaat - 14.8) < 0.5


def test_bmi_overgewicht():
    resultaat = bmi(90, 1.835)
    assert abs(resultaat - 26.7) < 0.5


def test_bmi_negatief_gewicht():
    resultaat = bmi(-1, 1.835)
    assert resultaat == -1


def test_bmi_negatieve_lengte():
    resultaat = bmi(80, -1.835)
    assert resultaat == -1


def test_bmi_0_lengte():
    resultaat = bmi(80, 0)
    assert resultaat == -1
