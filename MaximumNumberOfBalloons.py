"""
    Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

    You can use each character in text at most once. Return the maximum number of instances that can be formed.
"""

class MaximumNumberOfBalloons(object):
    def maxNumberOfBalloons(self, text):
        characters = {}
        singles = {'b', 'a', 'n'}
        characters['b'] = 0
        characters['a'] = 0
        characters['l'] = 0
        characters['o'] = 0
        characters['n'] = 0
        for i in range(0, len(text)):
            if text[i] in characters:
                characters[text[i]] += 1
        instances = 10000
        for i in characters:
            if i in singles:
                if characters[i] < instances:
                    instances = characters[i]
            elif characters[i] / 2 < instances:
                    instances = characters[i] / 2
        return instances