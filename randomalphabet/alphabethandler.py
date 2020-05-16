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

"""This module holds the AlphabetHandler class"""

import hashlib
import randomalphabet.repeatablerandom as rand
from randomalphabet.letterbucket import LetterBucket

class AlphabetHandler:
    """This class manages a seeded, pseudorandomly generated cipher"""
    
    def __init__(self):
        self._rand = rand.RepeatableRandom(0)
        self._alphabet = []
        self._value_list = []
        self._number_offset = 0

    def generate_alphabet(self, key, bucket_size=10):
        """
        Generates an alphabet from a key string and bucket size
        key - the key string
        bucket_size - an integer determining the number of encoded values associated with a given character (default=10)
        """
        if bucket_size < 1:
            raise ValueError('bucket_size must be greater than or equal to 1')

        try:
            digest = hashlib.sha512()
            digest.update(key.encode('latin1'))
            key_bytes = digest.digest()
            key_hashed_string = key_bytes.decode('latin1')
            self._rand = rand.RepeatableRandom(key_hashed_string)
            #self._rand.seed(0)
        except:
            raise Exception("Failed to generate alphabet")
        
        self._alphabet = []
        self._value_list = []

        for i in range(32, 127):
            self._alphabet.append(LetterBucket(chr(i)))
             
        self._alphabet.append(LetterBucket(chr(9)))
        self._alphabet.append(LetterBucket(chr(10)))
        self._alphabet.append(LetterBucket(chr(11)))
        self._alphabet.append(LetterBucket(chr(13)))
        
        for i in range(len(self._alphabet)*bucket_size):
            self._value_list.append(i)

        #self._rand.shuffle(self._value_list)
        for i, _ in enumerate(self._value_list):
            index = self._rand.next_int(0, len(self._value_list))
            temp = self._value_list[index]
            self._value_list[index] = self._value_list[i]
            self._value_list[i] = temp
        
        value_index = 0
        for i, _  in enumerate(self._alphabet):
            for j in range(bucket_size):
                self._alphabet[i].add_value(self._value_list[value_index])
                value_index += 1
        offset_index = self._rand.next_int(0, len(self._value_list))     
        self._number_offset = self._value_list[offset_index]
        #self._number_offset = 0
    def get_char_from_value(self, value):
        """
        Decodes a value and returns its corresponding character
        value - the encoded value to be decoded into a character
        """
        letter = "" 
        found = False
        for i, _ in enumerate(self._alphabet):
            if found:
                break
            if self._alphabet[i].contains_value(value):
                letter = self._alphabet[i].get_letter()
                found = True

        return letter

    def get_value_for_letter(self, letter):
        """
        Returns a randomly selected value associated with a character
        letter - the letter to be encoded
        """
        value = -1
        letter_found = False

        for i, _ in enumerate(self._alphabet):
            if letter_found:
                break
            if letter == self._alphabet[i].get_letter():
                value = self._alphabet[i].random_value()
                letter_found = True
        
        return value

    def get_value_for_number(self, number):
        """
        Returns the encoded value of a number
        number - the number to be encoded
        """
        return number + self._number_offset

    def get_number_for_value(self, value):
        """
        Returns the decoded number for a value
        value - the value to be decoded
        """
        return value - self._number_offset

    def random_value(self):
        """
        Returns a completely random value from the valid set
        This function is generally used to create decoys indistinguishable from a correct value
        """
        return self._value_list[self._rand.next_int(0,len(self._value_list))]
        
