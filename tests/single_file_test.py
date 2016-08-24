import pytest

from indexer.indexer import index


def test_sherlock_holmes():
    assert index('tests/sherlock_holmes.txt') == {'i': 3038, 'in': 1823,
                                                  'that': 1767, 'of': 2778,
                                                  'it': 1749, 'and': 3088,
                                                  'you': 1572, 'the': 5810,
                                                  'a': 2700, 'to': 2823}

def test_alice():
    assert index('tests/alice.txt') == {'it': 610, 'and': 940, 'a': 690,
                                       'to': 809, 'i': 545, 'you': 481,
                                       'the': 1818, 'she': 553, 'said': 462,
                                       'of': 631}
def test_sabotage():
    assert index('tests/sabotage.txt') == {'in': 226, 'you': 161, 'or': 233,
                                     'of': 382, 'will': 167, 'and': 355,
                                     'be': 168, 'the': 647, 'a': 302, 'to': 304}

