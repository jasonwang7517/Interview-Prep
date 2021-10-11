"""
Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""
from collections import defaultdict

class RansomNote(object):
    def canConstruct(self, ransomNote, magazine):
        letter_counts_magazine = defaultdict(int)
        letter_counts_note = defaultdict(int)
        for character in magazine:
            letter_counts_magazine[character] += 1
        for character in ransomNote:
            letter_counts_note[character] += 1
        for letter in letter_counts_note:
            if letter_counts_note[letter] > letter_counts_magazine[letter]:
                return False
        return True