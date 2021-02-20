class Solution(object):
    def countLargestGroup(self, n):
        sums = [0] * 37
        currMax = 0
        ans = 0
        for i in range(1, n + 1):
            sum = 0
            curr = str(i)
            for j in range(0, len(curr)):
                sum += int(curr[j])

            sums[sum] += 1

            if sums[sum] > currMax:
                ans = 1
                currMax = sums[sum]
            elif sums[sum] == currMax:
                ans += 1
        return ans
