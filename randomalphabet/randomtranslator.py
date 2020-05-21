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


"""This module holds the RandomTranslator class"""

import secrets as rand
from randomalphabet.alphabethandler import AlphabetHandler
from randomalphabet.ntuple import NTuple


class RandomTranslator:
    """This class to simplifies encoding and decoding text"""

    def __init__(self, key, bucket_size, decoy_count):
        """
        key - the key string to generate the alphabet
        bucket_size - the number of values associated with each character
        decoy_count - the number of decoys per tuple
        """
        self._decoy_count = decoy_count
        self._tuple_size = decoy_count + 3
        self._handler = AlphabetHandler()
        self._handler.generate_alphabet(key, bucket_size=bucket_size)

    def encode_text(self, text):
        """
        Returns encoded text
        text - the plaintext string to encode
        """
        tuple_list = []
        temp_array = [None] * (self._decoy_count + 1)
        temp_real_char_index = 0
        temp_location = 0
        encoded_text = ""

        try:
            for i, _ in enumerate(text):
                temp_real_char_index = rand.randbelow(len(temp_array))
                #temp_real_char_index = 0
                
                temp_location = self._handler.get_value_for_number(i)
                for j in range(self._decoy_count + 1):
                    temp_array[j] = self._handler.random_value()
                temp_array[temp_real_char_index] = self._handler.get_value_for_letter(text[i])
                tuple_list.append(
                    NTuple(temp_array.copy(), self._handler.get_value_for_number(temp_real_char_index), temp_location))
            
            for i, _ in enumerate(tuple_list):
                index = rand.randbelow(len(tuple_list))
                temp = tuple_list[index]
                tuple_list[index] = tuple_list[i]
                tuple_list[i] = temp
            
            encoded_text = ""
            for ntuple in tuple_list:
                temp_array = ntuple.get_values()
                temp_real_char_index = ntuple.get_index()
                temp_location = ntuple.get_location()
                
                for i in temp_array:
                    encoded_text += f'{i},'

                encoded_text += f'{temp_real_char_index},{temp_location},'
        except:
            raise Exception('Encoding failed')

        return encoded_text

    def decode_text(self, text):
        """
        Returns decoded text
        text - the text to decode
        """
        pieces = text.split(',')
        pieces.pop()

        decoded = [None] * (len(pieces)//self._tuple_size)

        temp_split = [None] * self._tuple_size
        temp_index = 0
        temp_letter = ""
        temp_location = 0

        penultimate = 0
        ultimate = 0

        try:
            i = 0
            while i < len(pieces):
                j = 0
                while j < len(temp_split):
                    temp_split[j] = pieces[i]
                    j += 1
                    i += 1
                penultimate = len(temp_split) - 2
                ultimate = len(temp_split) - 1
                temp_index = self._handler.get_number_for_value(int(temp_split[penultimate]))
                temp_letter = self._handler.get_char_from_value(int(temp_split[temp_index]))
                temp_location = self._handler.get_number_for_value(int(temp_split[ultimate]))
                decoded[temp_location] = temp_letter
        except:
            raise Exception('Decoding failed')
        
        decoded_string = ""
        return decoded_string.join(decoded)
