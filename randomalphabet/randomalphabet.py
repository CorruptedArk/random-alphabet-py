#!/usr/bin/env python3

"""This module is the main Random Alphabet script"""

import argparse
from randomalphabet.randomtranslator import RandomTranslator

def main():
    """Main function - this handles the overall purpose of the program"""
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["encode", "decode"], help="Whether input will be encoded or decoded")
    parser.add_argument("key", help="The key string to generate the alphabet")
    parser.add_argument("-f", "--file", help="This flag makes text treated as a file name", action="store_true")
    parser.add_argument("text", type=str, help="The text to encode or decode")
    parser.add_argument("-b", "--bucket_size", type=int, default=10, help="The number of values associated with a character")
    parser.add_argument("-d", "--decoy_count", type=int, default=2, help="The number of decoys in a tuple")

    args = parser.parse_args()
    
    translator = RandomTranslator(args.key, args.bucket_size, args.decoy_count)
    
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

