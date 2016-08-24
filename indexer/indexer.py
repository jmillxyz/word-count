"""Indexer.

Usage:
    indexer.py [-h] [FILE ...]

-h --help   show this

"""
import re
from docopt import docopt
from collections import Counter


def tokenize(text):
    """Tokenize a blob of text.

    Any character other than a-z, A-Z or 0-9 is assumed to be a delimiter.
    In Python regular expressions, \W is equivalent to all characters NOT
    in [a-zA-Z0-9_], so one must also add the underscore as an additional
    delimiter.

    Args:
        text (str): The string of text to tokenize.

    Returns:
        A list of every word from the input.

    """
    return re.split(pattern=r'[\W_]+', string=text)


def tabulate(word_list):
    """Track and count unique instances of each word from a list, ignoring case.

    Counter is a dictionary subclass for "counting hashable objects", in
    this case words. Since the spec doesn't explicitly say to convert the
    words in the list to case insensitive, we shouldn't mutate them
    permanently.

    Counter's most_common method returns the n most common elements and
    their counts, which is particularly useful. However, it returns a list,
    whereas a dict looks cleaner.

    Args:
        word_list (list): A list of words.

    Returns:
        A dictionary of the top 10 instances of a given word, ignoring case,
        ordered by frequency.

    """
    return dict(Counter(w.lower() for w in word_list).most_common(10))


def index(*files):
    """Tokenize and tabulate the 10 most common words from a list of text files.

    Build up a common word_list by tokenizing each file, combine the lists,
    then tabulate the entire result.

    Args:
        files (*args): The path (including filename) to one or more text files.

    Returns:
        A dictionary of the top 10 instances of a given word, ignoring case,
        ordered by frequency.
    """
    word_list = []
    for textfile in files:
        f = open(textfile)
        text = f.read()
        word_list += tokenize(text)
    return tabulate(word_list)


if __name__ == "__main__":
    args = docopt(__doc__)
    print(index(*args['FILE']))

