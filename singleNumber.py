class Solution(object):
    def singleNumber(self, nums):
        lastNum = set()
        for i in nums:
            if i not in lastNum:
                lastNum.add(i)
            elif i in lastNum:
                lastNum.remove(i)
        for i in lastNum:
            return i
