"""This module holds the LetterBucket class"""
#!/usr/bin/env python3

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
