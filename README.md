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

Indexer accepts one or more files as input, and returns a dictionary with the
top ten words with their frequencies.

```
$ python indexer/indexer.py FILE ...

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

This project is currently configured to run on Python 2.7, Python 3.4, and
Python 3.5.
