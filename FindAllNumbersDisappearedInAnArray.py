"""
    Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
"""

class FindAllNumbersDisappearedInAnArray(object):
    def findDisappearedNumbers(self, nums):
        ans = [0 for i in range(0, len(nums) + 1)]
        missing = [] 
        for i in nums:
            ans[i] = -1
        for i in range(1, len(ans)):
            if ans[i] == 0:
                missing.append(i)
        return missing
    # 1, 2, 2, 3, 3, 4, 7, 8