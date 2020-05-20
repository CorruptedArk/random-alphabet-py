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


"""This module is the main Random Alphabet script"""

import argparse
from randomalphabet.randomtranslator import RandomTranslator

MAJOR_VERSION = '0'
MINOR_VERSION = '1'
MICRO_VERSION = '2'
VERSION = "{}.{}.{}".format(MAJOR_VERSION, MINOR_VERSION, MICRO_VERSION)

ABOUT = f"""randomalphabet {VERSION} - Fork me at <https://github.com/CorruptedArk/random-alphabet-py>

random-alphabet-py is a command line tool to encode and decode text using a randomized cipher
  Copyright (C) 2020  Noah Stanford <noahstandingford@gmail.com>

  random-aphabet-py is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  random-alphabet-py is distributed in the hope that it will be interesting and useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


def get_version():
    """Returns the current version of the package"""
    return VERSION

def main():
    """Main function - this handles the overall purpose of the program"""
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description=ABOUT)
    parser.add_argument("action", choices=["encode", "decode"], help="Whether input will be encoded or decoded")
    parser.add_argument("key", help="The key string to generate the alphabet")
    parser.add_argument("-f", "--file", help="This flag makes text treated as a file name", action="store_true")
    parser.add_argument("text", type=str, help="The text to encode or decode")
    parser.add_argument("-b", "--bucket_size", type=int, default=10, help="The number of values associated with a character")
    parser.add_argument("-d", "--decoy_count", type=int, default=2, help="The number of decoys in a tuple")
    parser.add_argument('-v', '--version', action='version',
                    version=f'%(prog)s {VERSION}', help="Show program's version number and exit.")
    args = parser.parse_args()
    
    translator = RandomTranslator(args.key, args.bucket_size, args.decoy_count)
    
    if args.about:
        print(ABOUT)

    text_in = ""
    if args.file:
        text_file = open(args.text, 'r')
        text_in = text_file.read()
        text_file.close()
    else:
        text_in = args.text
        
    if args.action == 'encode':
        print(translator.encode_text(text_in))
    else:
        print(translator.decode_text(text_in))
        

if __name__ == '__main__':
    main()
