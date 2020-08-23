#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""
Mimic exercise

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read it into
one giant string and split it once.

Note: the standard python module 'random' includes a random.choice(list)
method which picks a random element from a non-empty list.

You can try adding in line breaks around 70 columns so the output looks
better.
"""

__author__ = """Anie Cross with help from instructor demo recordings,
Group-B discussion topics, Google search, docs.python.org, stackoverflow.com,
received help from 8/23/20 weekend Study Hall/tutor HPost"""


import random
import sys


def create_mimic_dict(filename):
    """Returns a dict mapping each word to a list of words which follow it.
    For example:
        Input: "I am a software developer, and I don't care who knows"
        Output:
            {
                "" : ["I"],
                "I" : ["am", "don't"],
                "am": ["a"],
                "a": ["software"],
                "software" : ["developer,"],
                "developer," : ["and"],
                "and" : ["I"],
                "don't" : ["care"],
                "care" : ["who"],
                "who" : ["knows"]
            }
    """

    f = open(filename, 'r')
    text = f.read()
    f.close()
    words = text.split()
    mimic_dict = {'': [words[0]]}
    for index in range(len(words) - 1):
        if index + 1 < len(words):
            if words[index] in mimic_dict.keys():
                mimic_dict[words[index]].append(words[index + 1])
            else:
                mimic_dict[words[index]] = [words[index + 1]]
    print(mimic_dict)
    return mimic_dict


def print_mimic_random(mimic_dict, num_words):
    """Given a previously created mimic_dict and num_words,
    prints random words from mimic_dict as follows:
    - Use a start_word of '' (empty string)
        - Print the start_word
        - Look up the start_word in your mimic_dict and get its next-list
        - Randomly select a new word from the next-list
        - Repeat this process num_words times
    """

    new_text = ''
    start_word = ''
    index = 0
    while index < num_words:
        random_word = random.choice(mimic_dict[start_word])
        new_text += random_word + ' '
        if random_word in mimic_dict:
            start_word = random_word
        else:
            start_word = ''
        index += 1
    print(new_text, end=' ')


def main(args):
    # Get input filename from command line args
    filename = args[0]

    # Create and print the jumbled (mimic) version of the input file
    print(f'Using {filename} as input:\n')
    d = create_mimic_dict(filename)
    print_mimic_random(d, 200)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
    else:
        main(sys.argv[1:])
    print('\n\nCompleted.')
