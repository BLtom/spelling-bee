# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 15:16:13 2021

@author: BLTom
"""

from collections import Counter
import sys
import time

with open('words.txt') as f:
    dictionary = f.read()

dictionary = [x.lower() for x in dictionary.split('\n')]


def return_anagrams(letters: str, must) -> list:

    global dictionary
    assert isinstance(letters,
                      str), 'Scrambled letters should only be of type string.'

    letters = letters.lower()

    letters_count = Counter(letters)

    anagrams = set()
    for word in dictionary:
        if not set(word) - set(letters):
            check_word = set()
            # Check if the count of each letter is less than or equal
            # to the count of that letter in scrambled letter input
            for k, v in Counter(word).items():
                if v <= letters_count[k]:
                    check_word.add(k)
            # Check if check_words is exactly equal to the unique letters
            # in the word of dictionary
            if check_word == set(word) and must in check_word and len(check_word)>3:
                anagrams.add(word)
    return sorted(list(anagrams), key=lambda x: len(x))


if __name__ == '__main__':
    start = time.time()
    test_anagrams = return_anagrams("clatiyu","u")
    print(test_anagrams)
    stop = time.time()
    print(f"Number of anagrams: {len(test_anagrams)}")
    print(f"Time Taken: {round(stop - start, 2)} seconds")