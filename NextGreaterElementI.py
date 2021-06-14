"""
    You are given two integer arrays nums1 and nums2 both of unique elements, where nums1 is a subset of nums2.

    Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

    The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, return -1 for this number.
"""

class NextGreaterElementI(object):
    def nextGreaterElement(self, nums1, nums2):
        hm = {}
        for i in range(0, len(nums2) - 1):
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    hm[nums2[i]] = nums2[j]
                    break
                if nums2[i] not in hm:
                    hm[nums2[i]] = -1
        hm[nums2[-1]] = -1
        ans = [0] * len(nums1)
        for i in range(0, len(nums1)):
            ans[i] = hm[nums1[i]]
        return ans
