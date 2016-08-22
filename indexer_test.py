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
