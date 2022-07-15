"""
Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of 
nums sorted in ascending order.
"""

class IntersectionOfMultipleArrays(object):
    def intersection(self, nums):
        index = 1
        ans = set(nums[0])
        while index < len(nums) and len(ans) > 0:
            to_remove = []
            for i in ans:
                if i not in nums[index]:
                    to_remove.append(i)
            for j in to_remove:
                ans.remove(j)
            index += 1
        final_ans = list(ans)
        final_ans.sort()
        return final_ans
                    
            
        