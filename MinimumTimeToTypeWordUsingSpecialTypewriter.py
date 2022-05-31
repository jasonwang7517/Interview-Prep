"""
There is a special typewriter with lowercase English letters 'a' to 'z' arranged in a circle with a pointer. 

A character can only be typed if the pointer is pointing to that character. The pointer is initially pointing to the character 'a'.
"""

class MinimumTimeToTypeWordUsingSpecialTypewriter(object):
    def minTimeToType(self, word):
        ans = 0
        curr = 'a'
        for i in word:
            diff = ord(i) - ord(curr)
            ans += min(abs(diff), 26 - abs(diff))
            ans += 1
            curr = i
        return ans