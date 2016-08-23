# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest

from indexer import tokenize, count_uniques


def test_tokenize_with_spaces():
    assert tokenize('Hello there friend') == ['Hello', 'there', 'friend']

def test_tokenize_with_commas():
    assert tokenize('my,spacebar,is,broken') == ['my', 'spacebar', 'is', 'broken']

def test_tokenize_with_mixed_characters():
    assert tokenize('This,sentence!is crazy') == ['This', 'sentence', 'is', 'crazy']

def test_tokenize_with_multiple_delimiters():
    assert tokenize('So    many    spaces') == ['So', 'many', 'spaces']

def test_tokenize_with_underscores():
    assert tokenize('So_many__underscores') == ['So', 'many', 'underscores']

def test_tokenize_numbers():
    assert tokenize('123_345 90!22*66') == ['123', '345', '90', '22', '66']

def test_tokenize_mix_alphanumeric():
    assert tokenize('123hello l33t__w0rds') == ['123hello', 'l33t', 'w0rds']

def test_tokenize_with_unicode_symbols():
    assert tokenize('Emoji🤓are👍fun') == ['Emoji', 'are', 'fun']

def test_uniques_for_same_word():
    assert count_uniques(['hello', 'hello', 'hello']) == {'hello':3}

def test_uniques_mixed_case():
    assert count_uniques(['mixed', 'MIXED', 'mixED']) == {'mixed':3}

def test_top_ten_items_only_are_returned():
    assert count_uniques(
        ['one', 'one', 'two', 'two', 'three', 'three', 'four', 'four', 'five',
         'five', 'six', 'six', 'seven', 'seven', 'eight', 'eight', 'nine',
         'nine', 'ten', 'ten', 'eleven']
    ) == {'one':2, 'two':2, 'three':2, 'four':2, 'five':2, 'six':2, 'seven':2,
          'eight':2, 'nine':2, 'ten':2}


