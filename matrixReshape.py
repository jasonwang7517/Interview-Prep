class Solution(object):
    def matrixReshape(self, nums, r, c):
        if (len(nums) * len(nums[0])) != (r * c):
            return nums
        newMatrix = [[0 for i in range(c)] for j in range (r)]
        values = []
        for i in nums:
            for j in i:
                values.append(j)
        index = 0
        for i in range(0, r):
            for j in range(0, c):
                newMatrix[i][j] = values[index]
                index += 1
        return newMatrix