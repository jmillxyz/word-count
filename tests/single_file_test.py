import pytest

@pytest.fixture(params=['tests/books/sherlock_holmes.txt'])
def sherlock():
     import indexer
     return indexer.indexer

def test_sherlock_holmes(sherlock):
    assert {'i': 3038, 'in': 1823, 'that': 1767, 'of': 2778, 'it': 1749,
            'and': 3088, 'you': 1572, 'the': 5810, 'a': 2700, 'to': 2823}

@pytest.fixture(params=['tests/books/alice.txt'])
def alice():
     import indexer
     return indexer.indexer

def test_alice(alice):
    assert {'it': 610, 'and': 940, 'a': 690, 'to': 809, 'i': 545, 'you': 481,
            'the': 1818, 'she': 553, 'said': 462, 'of': 631}

@pytest.fixture(params=['tests/books/sabotage.txt'])
def sabotage():
     import indexer
     return indexer.indexer

def test_sabotage(sabotage):
    assert {'in': 226, 'you': 161, 'or': 233, 'of': 382, 'will': 167,
            'and': 355, 'be': 168, 'the': 647, 'a': 302, 'to': 304}

