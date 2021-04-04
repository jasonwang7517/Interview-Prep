class Solution(object):
    def majorityElement(self, nums):
        currCount = 0
        currCandidate = None
        for i in nums:
            if currCount == 0:
                currCandidate = i
            if i == currCandidate:
                currCount += 1
            else:
                currCount -= 1
        return currCandidate