"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
"""

class WordPattern(object):
    def wordPattern(self, pattern, s):
        dic = {}
        seen = set()
        words = s.split(' ')
        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in dic and words[i] not in seen:
                dic[pattern[i]] = words[i]
                seen.add(words[i])
            elif (pattern[i] in dic and dic[pattern[i]] != words[i]) or (pattern[i] not in dic and words[i] in seen):
                return False
        return True
        