#!/usr/bin/env python3

"""This module holds the RepeatableRandom class"""

import hashlib

def create_generator(seed):
    """
    Returns a pseudorandom number generator
    seed - the seed string to generate a given sequence
    """
    hash_val = str.encode(seed)
    digest = hashlib.sha512()
    while True:
        digest.update(hash_val)
        hash_val = digest.digest()
        hash_num = int(digest.hexdigest(), 16)
        yield hash_num


class RepeatableRandom:
    """
    This class is used to generate reproducible sequences of random integers from a given seed string
    """
    def __init__(self, seed):
        """
        seed - The seed string. Each given seed produces a given sequence of numbers
        """
        self._generator = create_generator(seed)

    def next_int(self, start, stop):
        """
        Returns a pseudorandomly generated integer value
        start - the inclusive lower limit on the range
        stop - the exclusive upper limit on the range
        """
        return next(self._generator) % stop + start 
    
