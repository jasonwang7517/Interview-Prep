"""
    Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

    Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

    Return any answer array that satisfies this condition.
"""

class SortArrayByParityII(object):
    def sortArrayByParityII(self, A):
        odd = []
        even = []
        ans = [0] * len(A)
        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        for i in range(0, len(A)):
            if i % 2 == 0:
                ans[i] = even.pop()
            else:
                ans[i] = odd.pop()
        return ans
        
        