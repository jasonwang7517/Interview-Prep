"""
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at 
least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.
"""

from collections import defaultdict 

class MostCommonWord(object):
    def mostCommonWord(self, paragraph, banned):
        words = paragraph.split()
        counts = defaultdict(lambda: 0)
        symbols = "!?',;."
        for i in words:
            if i[-1] in symbols:
                i = i[:-1]
            if ',' in i:
                more_words = i.split(',')
                words.extend(more_words)
                continue
            counts[i.lower()] += 1
        for i in banned:
            counts[i] = 0
        return max(counts, key=counts.get)
        