import json
import subprocess
from sys import executable

import pytest

def transform_function_output(book_title):
    """Transform the bytestring from the subprocess.check_output() to a dict
    for comparison.

    Args:
        book_title (str): The abbreviation of the pytest.fixture param.

    Returns:
        A dictionary for comparison to previously-measured word frequencies.
    """
    cmd = "{:s} -m indexer {:s}".format(executable, book_title)
    result = subprocess.check_output(cmd.split())
    result = ''.join(result.decode())               # convert tuple of bytestrings to a string
    result = result.strip('\n').replace('\'','\"')  # remove newline, replace double quotes w/ single quotes
    frequency_dict = json.loads(result)             # convert string to python dict
    return frequency_dict

def test_sherlock_holmes_from_script():
    result = transform_function_output('tests/books/sherlock_holmes.txt')

    assert result == {'i': 3038, 'in': 1823, 'that': 1767, 'of': 2778,
                      'it': 1749, 'and': 3088, 'you': 1572, 'the': 5810,
                      'a': 2700, 'to': 2823}

def test_alice_from_script():
    result = transform_function_output('tests/books/alice.txt')

    assert result == {'it': 610, 'and': 940, 'a': 690, 'to': 809, 'i': 545,
                      'you': 481, 'the': 1818, 'she': 553, 'said': 462,
                      'of': 631}

def test_sabotage_from_script():
    result = transform_function_output('tests/books/sabotage.txt')

    assert result == {'in': 226, 'you': 161, 'or': 233, 'of': 382, 'will': 167,
                      'and': 355, 'be': 168, 'the': 647, 'a': 302, 'to': 304}

def test_alice_and_sabotage_from_script():
    result = transform_function_output('tests/books/sabotage.txt tests/books/alice.txt')

    assert result == {'a': 992, 'it': 715, 'and': 1295, 'i': 548, 'in': 657,
                      'of': 1013, 'she': 553, 'the': 2465, 'to': 1113,
                      'you': 642 }
