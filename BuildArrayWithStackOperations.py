"""
    Given an array target and an integer n. In each iteration, you will read a number from  list = {1,2,3..., n}.

    Build the target array using the following operations:
    - Push: Read a new element from the beginning list, and push it in the array.
    - Pop: delete the last element of the array.
    - If the target array is already built, stop reading more elements.

    Return the operations to build the target array. You are guaranteed that the answer is unique.
"""

class BuildArrayWithStackOperations(object):
    def buildArray(self, target, n):
        index = 0
        curr = 1
        ans = []
        while index < len(target):
            if curr < target[index]:
                ans.append("Push")
                ans.append("Pop")
                curr += 1
            elif curr == target[index]:
                ans.append("Push")
                curr += 1
                index += 1
        return ans
        