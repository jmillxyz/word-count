import re
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

def count_uniques(word_list):
    """Track unique instances of each word from a list, ignoring case.

    Counter is a dictionary subclass for "counting hashable objects", in
    this case words. Since the spec doesn't explicitly say to convert the
    words in the list to case insensitive, we shouldn't mutate them
    permanently.

    Counter's most_common method returns the n most common elements and
    their counts, which is particularly useful. However, it returns a list,
    whereas the dict looks better.

    Args:
        word_list (list): A list of words.

    Returns:
        A dictionary of the top 10 instances of a given word, ignoring case,
        ordered by frequency.

    """
    return dict(Counter(w.lower() for w in word_list).most_common(10))

