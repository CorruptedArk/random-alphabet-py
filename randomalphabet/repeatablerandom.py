#!/usr/bin/env python3

# random-alphabet-py is a command line tool to encode and decode text using a randomized cipher
#   Copyright (C) 2020  Noah Stanford <noahstandingford@gmail.com>
# 
#   random-aphabet-py is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
# 
#   random-alphabet-py is distributed in the hope that it will be interesting and useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
# 
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.


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
