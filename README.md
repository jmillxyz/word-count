# Indexer.py

[![Build Status](https://travis-ci.org/jondelmil/word-count.svg?branch=master)](https://travis-ci.org/jondelmil/word-count)
[![Coverage Status](https://coveralls.io/repos/github/jondelmil/word-count/badge.svg?branch=master)](https://coveralls.io/github/jondelmil/word-count?branch=master)

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
$ python -m indexer <file>...
```

For example, to see most common words in _Alice in Wonderland_:
```
$ python -m indexer tests/books/alice.txt
{'to': 809, 'the': 1818, 'she': 553, 'said': 462, 'of': 631, 'you': 481, 'and':
940, 'i': 545, 'a': 690, 'it': 610}
```

To see the most common words in both _Alice in Wonderland_ and _Simple Sabotage
Field Manual_, list the path to both titles, separated by a space.

```
$ python -m indexer tests/books/alice.txt tests/books/sabotage.txt
{'a': 992, 'it': 715, 'and': 1295, 'i': 548, 'in': 657, 'of': 1013, 'she': 553,
'the': 2465, 'to': 1113, 'you': 642 }
```

### Advanced Usage

You can also specify the number of workers to use for a given task with the
`-w <w>` or `--workers <w>` options, where `<w>` is an integer. Keep in mind that
there will only be as many workers instantiated as there are files to parse.

For example,
```
$ python -m indexer -w 5 tests/books/sabotage.txt
```
specifies 5 workers, but only one will be used to read and tokenize since only
one file is used.

Non-integer values for `<w>` will be ignored, and will default to use up to the
maximum number of cores on the host machine. If more files are specified than
the host machine has cores, the workers will be reused for remaining jobs. For
instance, on my 8-core machine, 9 files are handled like so:
```
$ python -m indexer tests/books/alice.txt tests/books/alice.txt
tests/books/alice.txt tests/books/alice.txt tests/books/alice.txt
tests/books/alice.txt tests/books/alice.txt tests/books/alice.txt
tests/books/alice.txt
<ForkProcess(ForkPoolWorker-1, started daemon)> reading tests/books/alice.txt
<ForkProcess(ForkPoolWorker-2, started daemon)> reading tests/books/alice.txt
<ForkProcess(ForkPoolWorker-3, started daemon)> reading tests/books/alice.txt
<ForkProcess(ForkPoolWorker-4, started daemon)> reading tests/books/alice.txt
<ForkProcess(ForkPoolWorker-5, started daemon)> reading tests/books/alice.txt
<ForkProcess(ForkPoolWorker-6, started daemon)> reading tests/books/alice.txt
<ForkProcess(ForkPoolWorker-7, started daemon)> reading tests/books/alice.txt
<ForkProcess(ForkPoolWorker-8, started daemon)> reading tests/books/alice.txt
<ForkProcess(ForkPoolWorker-1, started daemon)> reading tests/books/alice.txt
{'the': 16362, 'and': 8460, 'of': 5679, 'said': 4158, 'she': 4977, 'you': 4329,
'i': 4905, 'it': 5490, 'a': 6210, 'to': 7281}
```
A `print` statement has been added in the above example to demonstrate the
multiprocessing pool properties. As shown above, using the same file more than
once is permitted. The indexer will simply count all words again, as if each
file was a different document.

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

