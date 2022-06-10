"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.
"""

class ReverseVowelsOfString(object):
    def reverseVowels(self, s):
        ans = []
        stack = []
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        for i in s:
            if i in vowels:
                stack.append(i)
                ans.append('_')
            else:
                ans.append(i)
        for i in range(len(ans)):
            if ans[i] == '_':
                ans[i] = stack.pop()
        return ''.join(ans)