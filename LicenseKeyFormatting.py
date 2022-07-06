"""
You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an 
integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. 
Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.
"""

class LicenseKeyFormatting(object):
    def licenseKeyFormatting(self, s, k):
        q = []
        for i in s:
            if i != '-':
                q.append(i.upper())
        first_group_size = len(q) % k
        ans = []
        if first_group_size > 0:
            for i in range(first_group_size):
                ans.append(q.pop(0))
            ans.append('-')
        letters_added = 0
        while len(q) > 0:
            ans.append(q.pop(0))
            letters_added += 1
            if letters_added == k:
                ans.append('-')
                letters_added = 0
        if len(ans) > 0:
            ans.pop(-1)
        return ''.join(ans)
            
        