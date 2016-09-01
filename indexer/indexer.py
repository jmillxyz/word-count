"""Common words indexer.

Grab the 10 most common words from one or more files!

Usage:
  indexer [--workers <w> | -w <w>] <file>...
  indexer (-h | --help)
  indexer (-v | --version)

Options:
  -w <w>, --workers <w>  Specify number of possible workers, up to host's max. None means to use up to all cores. [default: 0]
  -v, --version          Show version of this program.
  -h --help              Show this screen.

"""
import re
import argparse
import multiprocessing
from itertools import chain
from collections import Counter

from docopt import docopt

from .mapper import Mapper


def read(filename):
    """Read a file.

    Notify the user via console which process is reading each filename.

    Args:
        filename (str): Path to a file.

    Returns:
        A string containing all of the text in that file.

    """
    f = open(filename, 'r')
    ## show the process and which file it's reading
    # print(multiprocessing.current_process(), 'reading', filename)
    text = f.read()
    return text

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

def tabulate(word_list, num_words=10):
    """Track and count unique instances of each word from a list, ignoring case.

    If num_words is not provided, default to 10.

    Args:
        word_list (list): A list of words.

    Returns:
        An unsorted dictionary of the top num_words instances of a given word,
        ignoring case.

    """
    return dict(Counter(w.lower() for w in word_list).most_common(num_words))

def flatten(word_list):
    """Flatten 2-D list into a single list.

    Args:
        word_list (list): A list of word lists.

    Returns:
        A flattened/unrolled list with all of the same inner elements.

    """
    return list(chain.from_iterable(word_list))

def main():
    """Main program entry point.

    Parse command line arguments, kick off tokenize/tabulate/flatten commands,
    and print result.
    """
    args = docopt(__doc__, version=0.1)
    files = args['<file>']
    try:
        num_workers = int(args['--workers'])
        mapper = Mapper(read, tokenize, num_workers)
    except:
        mapper = Mapper(read, tokenize)
    all_word_lists = mapper(files)
    flattened_word_list = flatten(all_word_lists)
    top10_words = tabulate(flattened_word_list, 10)
    print(top10_words)

