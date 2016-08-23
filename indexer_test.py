import pytest

from indexer import Indexer


def test_tokenize_with_spaces():
    assert Indexer.tokenize('Hello there friend') == ['Hello', 'there', 'friend']

def test_tokenize_with_commas():
    assert Indexer.tokenize('my,spacebar,is,broken') == ['my', 'spacebar', 'is', 'broken']

def test_tokenize_with_mixed_characters():
    assert Indexer.tokenize('This,sentence!is crazy') == ['This', 'sentence', 'is', 'crazy']

def test_tokenize_with_multiple_delimiters():
    assert Indexer.tokenize('So    many    spaces') == ['So', 'many', 'spaces']

def test_tokenize_with_underscores():
    assert Indexer.tokenize('So_many__underscores') == ['So', 'many', 'underscores']

def test_tokenize_numbers():
    assert Indexer.tokenize('123_345 90!22*66') == ['123', '345', '90', '22', '66']

def test_tokenize_mix_alphanumeric():
    assert Indexer.tokenize('123hello l33t__w0rds') == ['123hello', 'l33t', 'w0rds']

def test_tokenize_with_unicode_symbols():
    assert Indexer.tokenize('Emoji🤓are👍fun') == ['Emoji', 'are', 'fun']

def test_uniques_for_same_word():
    assert Indexer.count_uniques(['hello', 'hello', 'hello']) == {'hello':3}

def test_uniques_mixed_case():
    assert Indexer.count_uniques(['mixed', 'MIXED', 'mixED']) == {'mixed':3}

def test_top_ten_items_only_are_returned():
    assert Indexer.count_uniques(
        ['one', 'one', 'two', 'two', 'three', 'three', 'four', 'four', 'five',
         'five', 'six', 'six', 'seven', 'seven', 'eight', 'eight', 'nine',
         'nine', 'ten', 'ten', 'eleven']
    ) == {'one':2, 'two':2, 'three':2, 'four':2, 'five':2, 'six':2, 'seven':2,
          'eight':2, 'nine':2, 'ten':2}


