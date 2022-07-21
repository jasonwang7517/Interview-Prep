"""
You are given a 0-indexed integer array nums. In one operation, you may do the following:
    - Choose two integers in nums that are equal.
    - Remove both integers from nums, forming a pair.
    - The operation is done on nums as many times as possible.

Return a 0-indexed integer array answer of size 2 where answer[0] is the number of pairs that are formed and answer[1] is the number of leftover integers in nums 
after doing the operation as many times as possible.
"""

from collections import defaultdict

class MaximumNumberOfPairsInArray(object):
    def numberOfPairs(self, nums):
        pairs = defaultdict(lambda: 0)
        for i in nums:
            pairs[i] += 1
        ans = 0
        remainder = 0
        print(pairs)
        for i in pairs:
            ans += pairs[i] // 2
            remainder += pairs[i] % 2 
        return [ans, remainder]