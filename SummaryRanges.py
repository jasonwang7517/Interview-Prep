"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, 
and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:
    - "a->b" if a != b
    - "a" if a == b
"""

class SummaryRanges(object):
    def summaryRanges(self, nums):
        ans = []
        if len(nums) == 0:
            return ans
        if len(nums) == 1:
            ans.append(str(nums[0]))
            return ans
        left = 0
        right = 1
        while right < len(nums):
            while nums[right] - nums[right - 1] <= 1:
                right += 1
                if right >= len(nums):
                    break
            st = str(nums[left])
            if right - left > 1:
                st = st + "->" + str(nums[right - 1])
            ans.append(st)
            left = right
            right += 1
        if left < len(nums):
            if right - left <= 1:
                ans.append(str(nums[left]))
            else:
                st = str(nums[left]) + "->" + str(nums[right - 1])
        return ans