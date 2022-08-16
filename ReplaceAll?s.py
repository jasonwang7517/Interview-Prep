"""
Given a string s containing only lowercase English letters and the '?' character, convert all the '?' characters into lowercase letters such that the 
final string does not contain any consecutive repeating characters. 

You cannot modify the non '?' characters.

It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them. 

It can be shown that an answer is always possible with the given constraints.
"""

class ReplaceToAvoidConsecutiveRepeatingCharacters(object):
    def modifyString(self, s):
        if len(s) == 1:
            return "a"
        ans = list(s)
        for i in range(len(ans)):
            if ans[i] == '?':
                chars_to_change = []
                if i > 0 and i < len(ans) - 1:
                    chars_to_change.append(ans[i - 1])
                    chars_to_change.append(ans[i + 1])
                elif i == 0:
                    chars_to_change.append(ans[i + 1])
                elif i == len(ans) - 1:
                    chars_to_change.append(ans[i - 1])
                new_ch = self.generate_new_char(chars_to_change)
                ans[i] = new_ch
        return ''.join(ans)
                    
    def generate_new_char(self, chars):
        current = set(chars)
        for i in range(97, 123):
            if chr(i) not in current:
                return chr(i)
        
