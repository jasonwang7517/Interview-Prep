"""
You are given a non-negative integer array nums. In one operation, you must:
    - Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
    - Subtract x from every positive element in nums.

Return the minimum number of operations to make every element in nums equal to 0.
"""

class MakeArrayZeroBySubtractingEqualAmounts(object):
    def minimumOperations(self, nums):
        vals = set(nums)
        ans = len(vals)
        return ans - 1 if 0 in vals else ans        