import re
from collections import Counter


def tokenize(text:str) -> list:
    '''
    Tokenize a blob of text.

    Any character other than a-z, A-Z or 0-9 is assumed to be a delimiter.
    In Python regular expressions, \W is equivalent to all characters NOT
    in [a-zA-Z0-9_], so one must also add the underscore as an additional
    delimiter.
    '''
    return re.split(pattern=r'[\W_]+', string=text)

def count_uniques(word_list:list) -> dict:
    """
    Track unique instances of each word from a list, ignoring case.

    Counter is a dictionary subclass for "counting hashable objects", in
    this case words. Since the spec doesn't explicitly say to convert the
    words in the list to case insensitive, we shouldn't mutate them
    permanently.

    Counter's most_common method returns the n most common elements and
    their counts, which is particularly useful. However, it returns a list,
    whereas the dict looks better.
    """
    return dict(Counter(w.lower() for w in word_list).most_common(10))

