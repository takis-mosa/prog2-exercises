def is_prime(x):
    """Geef True als x een priemgetal is, anders False

    Een priemgetal is een getal groter dan 1, dat geen product
    is van twee kleinere natuurlijke getallen.
    Oftewel, dat slechts twee natuurlijke getallen als deler heeft, namelijk 1
    en zichzelf.

    https://nl.wikipedia.org/wiki/Priemgetal
    https://www.eff.org/press/archives/2009/10/14-0
    """
    return 0


def fibonacci(n):
    """Geef het n-de getal in de rij van Fibonacci terug

    De rij van Fibonacci getallen zijn:
    0, 1, 1, 2, 3, 5, 8, ...

    Hierbij is elk volgend getal, de som van de twee
    voorgaande getallen:
    0 + 1 = 1
    1 + 1 = 2
    1 + 2 = 3
    2 + 3 = 5
    3 + 5 = 8
    ...

    https://nl.wikipedia.org/wiki/Rij_van_Fibonacci
    """
    return 0


def rekeningnummer_controlegetal(n):
    """Geef het controlegetal terug van rekeningnummer n

    Het controlegetal is het getal gevormd door de laatste
    twee cijfers van het rekeningnummer.

    Voor het rekeningnummer van Touring is dit bijvoorbeeld 49:
    068-9099786-49
    """
    return 0


def rekeningnummer_hoofdgetal(n):
    """Geef het hoofdgetal terug van rekeningnummer n

    Het hoofdgetal is het getal gevormd door de eerste
    tien cijfers van het rekeningnummer.

    Voor het rekeningnummer van Touring is dit bijvoorbeeld:
    Gegeven 068-9099786-49, dient het resultaat 689099786 te zijn.

    Voor het rekeningnummer van Telenet is dit bijvoorbeeld:
    Gegeven 405-0504611-48, dient het resultaat 4050504611 te zijn.
    """
    return 0


def is_geldig_rekeningnummer(n):
    """Geef True terug als het rekeningnummer geldig is, anders False.

    Een rekeningnummer is geldig als de deling van het hoofdgetal
    door 97 als rest het controlegetal geeft.

    Voor het rekeningnummer van Touring is dit bijvoorbeeld:
    Gegeven 068-9099786-49, dient de rest bij deling van 689099786 door 97
    49 te zijn.

    Voor het rekeningnummer van Telenet is dit bijvoorbeeld:
    Gegeven 405-0504611-48, dient de rest bij deling van 4050504611 door 97
    48 te zijn.
    """
    return 0


def is_anagram(word1, word2):
    """Return True word1 een anagram is van word2.

    Word1 is een anagram van word2 als het gevormd
    is uit de letters van word2, maar met de letters
    in een andere volgorde.

    Voorbeelden van anagrammen:
    - "top", "pot"
    - "listen", "silent"
    - "evil", "vile"

    Spaties worden genegeerd:
    - "forty five" = "over fifty"
    - "eleven plus two" = "twelve plus one"

    En ook hoofdletters worden genegeerd:
    - "Santa" = "Satan"

    Dus, in onderstaand voorbeeld moeten zowel de hoofdletters als de spaties
    genegeerd worden:
    - "William Shakespeare" = "I am a weakish speller"

    https://nl.wikipedia.org/wiki/Anagram
    """
    return 0
