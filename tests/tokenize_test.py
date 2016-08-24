# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest

from indexer.indexer import tokenize


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

