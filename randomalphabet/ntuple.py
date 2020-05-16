#!/usr/bin/env python3

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
