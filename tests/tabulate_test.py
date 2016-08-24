import pytest

from indexer.indexer import tabulate


def test_uniques_for_same_word():
    assert tabulate(['hello', 'hello', 'hello']) == {'hello':3}

def test_uniques_mixed_case():
    assert tabulate(['mixed', 'MIXED', 'mixED']) == {'mixed':3}

def test_top_ten_items_only_are_returned():
    assert tabulate(
        ['one', 'one', 'two', 'two', 'three', 'three', 'four', 'four', 'five',
         'five', 'six', 'six', 'seven', 'seven', 'eight', 'eight', 'nine',
         'nine', 'ten', 'ten', 'eleven']
    ) == {'one':2, 'two':2, 'three':2, 'four':2, 'five':2, 'six':2, 'seven':2,
          'eight':2, 'nine':2, 'ten':2}

