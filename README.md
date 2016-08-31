# Indexer.py

[![Build Status](https://travis-ci.com/jondelmil/rackspace-interview.svg?token=DWs7Yq7X3tMvJwqPZewY&branch=master)](https://travis-ci.com/jondelmil/rackspace-interview)

Grab the top 10 most common words from a list of files.

## Installation

It's preferable to install these dependencies in a
[virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/). All
commands in this document should be executed from the root level directory of
the project.

```
$ pip install -r requirements.txt
```

## Usage

Indexer accepts one or more paths to files as input, and returns a dictionary
containing the top ten words with their frequencies.

```
$ python -m indexer FILE FILE2 ...
```

For example, to see most common words in _Alice in Wonderland_:
```
$ python -m indexer tests/books/alice.txt
{'to': 809, 'the': 1818, 'she': 553, 'said': 462, 'of': 631, 'you': 481, 'and':
940, 'i': 545, 'a': 690, 'it': 610}
```


## Development

To install development dependencies locally:
```
pip install -r requirements-dev.txt
```

To test locally:
```
tox
```

Tests will automatically run on [Travis
CI](https://travis-ci.com/jondelmil/rackspace-interview) once pushed to GitHub.

This project will run on Python 2.7, Python 3.4, and Python 3.5.

## Rackspace Notes

This project has been extended to execute concurrently using Python's
`multiprocessing` library (specifically the `Pool` class), which by default will
use up to the host's max number of CPU cores as the number of workers (but no
more than the number of text files sent to be indexed).

