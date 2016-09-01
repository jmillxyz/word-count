import json
import subprocess
from sys import executable

import pytest

def transform_function_output(num_workers, book_title):
    """Transform the bytestring from the subprocess.check_output() to a dict
    for comparison.

    Args:
        book_title (str): The abbreviation of the pytest.fixture param.

    Returns:
        A dictionary for comparison to previously-measured word frequencies.
    """
    cmd = "{:s} -m indexer -w {:s} {:s}".format(executable, num_workers, book_title)
    result = subprocess.check_output(cmd.split())
    result = ''.join(result.decode())               # convert tuple of bytestrings to a string
    result = result.strip('\n').replace('\'','\"')  # remove newline, replace double quotes w/ single quotes
    frequency_dict = json.loads(result)             # convert string to python dict
    return frequency_dict

def test_same_output_from_one_or_two_workers():
    zero_workers = transform_function_output('0', 'tests/books/sherlock_holmes.txt')
    one_worker = transform_function_output('1', 'tests/books/sherlock_holmes.txt')
    two_workers = transform_function_output('2', 'tests/books/sherlock_holmes.txt')
    hundred_workers = transform_function_output('100', 'tests/books/sherlock_holmes.txt')

    assert zero_workers == {'i': 3038, 'in': 1823, 'that': 1767, 'of': 2778,
                      'it': 1749, 'and': 3088, 'you': 1572, 'the': 5810,
                      'a': 2700, 'to': 2823}
    assert zero_workers == one_worker
    assert one_worker == two_workers
    assert two_workers == hundred_workers

