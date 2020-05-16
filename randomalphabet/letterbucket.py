#!/usr/bin/env python3

"""This module holds the LetterBucket class"""

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

import secrets as rand

class LetterBucket:
    """LetterBucket is a class to manage the number values associated with a character in cipher"""
    def __init__(self, letter):
        self.letter = letter
        self.values = []
        
    def add_value(self, value):
        """
        This function adds a value to the bucket
        value - the value to be added
        """
        self.values.append(value)

    def contains_value(self, value):
        """
        This function checks if a value exists in the bucket returning True if it does and False otherwise
        value - the value to be checked
        """

        contains = False

        for i in range(len(self.values)):
            if contains:
                break
            contains = value == self.values[i]

        return contains

    def get_letter(self):
        """This function returns the letter associated with the bucket"""
        return self.letter

    def random_value(self):
        """This function returns a randomly selected value from the bucket"""
        return rand.choice(self.values)
