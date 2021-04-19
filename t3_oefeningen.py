import math

def bmi(gewicht, lengte):
    resultaat = gewicht / (lengte**2)
    return resultaat

def omtrek_cirkel(r):
    resultaat = 2 * r * math.pi
    return resultaat

def oppervlakte_cirkel(r):
    resultaat = r**2 * math.pi
    return resultaat

def oppervlakte_vierkant(zijde):
    resultaat = zijde**2
    return resultaat

def volume_cilinder(r, h):
    resultaat = math.pi * r**2 * h
    return resultaat

def volume_kubus(zijde):
    resultaat = zijde**3
    if resultaat < 0:
        resultaat = 0
        return resultaat
    else:
        return resultaat