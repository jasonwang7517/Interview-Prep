class Solution(object):
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
