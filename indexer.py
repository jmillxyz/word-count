import re

class Indexer:

    def tokenize(text:str) -> list:
        '''
        Tokenize a blob of text.

        Any character other than a-z, A-Z or 0-9 is assumed to be a delimiter.
        In Python regular expressions, \W is equivalent to all characters not
        in [a-zA-Z0-9_], so one must also add the underscore as an additional
        delimiter.
        '''
        return re.split(pattern=r'[\W_]+', string=text)

    def track(word_list:list) -> dict:
        pass
