import pytest

from t3_oefeningen_3 import (
    is_prime,
    is_anagram,
    fibonacci,
    rekeningnummer_controlegetal,
    rekeningnummer_hoofdgetal,
    is_geldig_rekeningnummer,
)


def test_is_prime_2():
    result = is_prime(2)
    assert result is True


def test_is_prime_3():
    result = is_prime(3)
    assert result is True


def test_is_prime_4():
    result = is_prime(4)
    assert result is False


def test_is_prime_5():
    result = is_prime(5)
    assert result is True


TESTDATA_PRIMES = [
    (6, False),
    (7, True),
    (8, False),
    (9, False),
    (10, False),
    (11, True),
    (12, False),
    (13, True),
    (14, False),
    (15, False),
    (16, False),
    (17, True),
]


@pytest.mark.parametrize("n,expected", TESTDATA_PRIMES)
def test_are_prime_numbers(n, expected):
    result = is_prime(n)
    assert result is expected


def test_fibonacci_1():
    result = fibonacci(1)
    assert result == 0


def test_fibonacci_2():
    result = fibonacci(2)
    assert result == 1


def test_fibonacci_3():
    result = fibonacci(3)
    assert result == 1


def test_fibonacci_4():
    result = fibonacci(4)
    assert result == 2


def test_fibonacci_5():
    result = fibonacci(5)
    assert result == 3


def test_fibonacci_6():
    result = fibonacci(6)
    assert result == 5


TESTDATA_FIBONACCI = [
    (7, 8),
    (8, 13),
    (9, 21),
    (10, 34),
    (11, 55),
    (12, 89),
    (13, 144),
    (14, 233),
    (15, 377),
    (16, 610),
]


@pytest.mark.parametrize("n,expected", TESTDATA_FIBONACCI)
def test_fibonacci_numbers(n, expected):
    result = fibonacci(n)
    assert result == expected


RN_BELFIUS = "091-0122401-16"
RN_EDPNET = "293-0436422-74"
RN_PROXIMUS = "000-1710031-18"
RN_TELENET = "405-0504611-48"


def test_rekeningnummer_controlegetal_telenet():
    result = rekeningnummer_controlegetal(RN_TELENET)
    assert result == 48


def test_rekeningnummer_controlegetal_edpnet():
    result = rekeningnummer_controlegetal(RN_EDPNET)
    assert result == 74


def test_rekeningnummer_controlegetal_proximus():
    result = rekeningnummer_controlegetal(RN_PROXIMUS)
    assert result == 18


def test_rekeningnummer_controlegetal_belfius():
    result = rekeningnummer_controlegetal(RN_BELFIUS)
    assert result == 16


def test_rekeningnummer_hoofdgetal_telenet():
    result = rekeningnummer_hoofdgetal(RN_TELENET)
    assert result == 4050504611


def test_rekeningnummer_hoofdgetal_belfius():
    result = rekeningnummer_hoofdgetal(RN_BELFIUS)
    assert result == 910122401


def test_rekeningnummer_hoofdgetal_proximus():
    result = rekeningnummer_hoofdgetal(RN_PROXIMUS)
    assert result == 1710031


def test_rekeningnummer_hoofdgetal_edpnet():
    result = rekeningnummer_hoofdgetal(RN_EDPNET)
    assert result == 2930436422


def test_telenet():
    result = is_geldig_rekeningnummer(RN_TELENET)
    assert result is True


def test_belfius():
    result = is_geldig_rekeningnummer(RN_BELFIUS)
    assert result is True


def test_proximus():
    result = is_geldig_rekeningnummer(RN_PROXIMUS)
    assert result is True


def test_edpnet():
    result = is_geldig_rekeningnummer(RN_EDPNET)
    assert result is True


def test_telenet_false():
    result = is_geldig_rekeningnummer("405-0504611-42")
    assert result is False


def test_proximus_false():
    result = is_geldig_rekeningnummer("001-1710031-18")
    assert result is False


def test_edpnet_false():
    result = is_geldig_rekeningnummer("293-0436422-84")
    assert result is False


def test_belfius_false():
    result = is_geldig_rekeningnummer("081-0122401-16")
    assert result is False


def test_is_anagram():
    result = is_anagram("listen", "silent")
    assert result is True


def test_is_geen_anagram():
    result = is_anagram("konijn", "ezel")
    assert result is False


TESTDATA_ANAGRAMS = [
    ("tar", "rat"),
    ("elbow", "below"),
    ("night", "thing"),
    ("inch", "chin"),
    ("state", "taste"),
    ("evil", "vile"),
    ("santa", "satan"),
    ("herman", "arnhem"),
    ("koelkast", "kakstoel"),
    ("schollevaar", "aalscholver"),
]


@pytest.mark.parametrize("word1,word2", TESTDATA_ANAGRAMS)
def test_are_anagrams(word1, word2):
    result = is_anagram(word1, word2)
    assert result is True


TESTDATA_NOT_ANAGRAMS = [
    ("ter", "rat"),
    ("elbow", "blow"),
    ("night", "hing"),
    ("inch", "chon"),
    ("state", "toste"),
    ("evil", "vyle"),
    ("santa", "saton"),
    ("herman", "arnhim"),
    ("koelkast", "kakstoul"),
    ("schollevaar", "ealscholver"),
]


@pytest.mark.parametrize("word1,word2", TESTDATA_NOT_ANAGRAMS)
def test_are_not_anagrams(word1, word2):
    result = is_anagram(word1, word2)
    assert result is False


TESTDATA_ANAGRAMS_SPACES = [
    ("new york times", "monkeys write", True),
    ("new york times", "mankeys write", False),
    ("william shakespeare", "i am a weakish speller", True),
    ("william shakespeare", "i em a weakish speller", False),
    ("het beleg van laken", "gek leven na het bal", True),
    ("het beleg van laken", "gek leven na de bal", False),
]


@pytest.mark.parametrize("word1,word2,expected", TESTDATA_ANAGRAMS_SPACES)
def test_are_noanagrams_ignore_spaces(word1, word2, expected):
    result = is_anagram(word1, word2)
    assert result is expected


TESTDATA_ANAGRAMS_SPACES_CASE = [
    ("New York Times", "monkeys write", True),
    ("New York Times", "monkeys wrote", False),
    ("William Shakespeare", "I am a weakish speller", True),
    ("William Shakespeare", "I am a weakesh speller", False),
    ("Het beleg van Laken", "Het leven na beklag", True),
    ("Het beleg van Laken", "Het leven na het beklag", False),
]


@pytest.mark.parametrize("word1,word2,expected", TESTDATA_ANAGRAMS_SPACES_CASE)
def test_are_anagrams_ignore_spaces_and_case(word1, word2, expected):
    result = is_anagram(word1, word2)
    assert result is expected
