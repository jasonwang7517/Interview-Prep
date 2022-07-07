"""
You are given a string word that consists of digits and lowercase English letters.

You will replace every non-digit character with a space. For example, "a123bc34d8ef34" will become " 123  34 8  34". Notice that you are left with some integers that are separated by 
at least one space: "123", "34", "8", and "34".

Return the number of different integers after performing the replacement operations on word.

Two integers are considered different if their decimal representations without any leading zeros are different.
"""

class NumberOfDifferentIntegersInAString(object):
    def numDifferentIntegers(self, word):
        seen = set()
        current = []
        for i in word:
            if i >= '0' and i <= '9':
                current.append(i)
            else:
                if len(current) != 0:
                    to_add = ''.join(current)
                    seen.add(int(to_add))
                    current = []
        if len(current) != 0:
            to_add = ''.join(current)
            seen.add(int(to_add))
            current = []
        return len(seen)
        