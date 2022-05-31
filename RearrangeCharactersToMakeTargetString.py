"""
You are given two 0-indexed strings s and target. You can take some letters from s and rearrange them to form new strings.

Return the maximum number of copies of target that can be formed by taking letters from s and rearranging them.
"""

from collections import defaultdict

class Solution(object):
    def rearrangeCharacters(self, s, target):
        counts = defaultdict(lambda: 0)
        for i in s:
            counts[i] += 1
        target_counts = defaultdict(lambda: 0)
        for i in target:
            target_counts[i] += 1
            
        ans = float('inf')
        for i in target_counts:
            ans = min(ans, counts[i] // target_counts[i])
        return ans