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


"""This module contains the NTuple class"""

class NTuple:
    """This class manages the structure of tuples in encoded text"""
    def __init__(self, values, penultimate, ultimate):
        """
        values - a list of encoded letters with decoys
        penultimate - the second to last encoded number in the tuple
        ultimate - the last encoded number in the tuple
        """
        self._values = values
        self._index = penultimate
        self._location = ultimate

    def get_values(self):
        """Returns the the list of encoded letters with decoys"""
        return self._values

    def get_index(self):
        """Returns the index of the correct character to decode in the value list"""
        return self._index

    def get_location(self):
        """Returns the proper location of the character in the final decoded message string"""
        return self._location
