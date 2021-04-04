class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        currMax = releaseTimes[0]
        ans = keysPressed[0]
        for i in range(1, len(keysPressed)):
            if releaseTimes[i] - releaseTimes[i - 1] > currMax:
                ans = keysPressed[i]
                currMax = releaseTimes[i] - releaseTimes[i - 1]
            elif releaseTimes[i] - releaseTimes[i - 1] == currMax:
                if keysPressed[i] > ans:
                    ans = keysPressed[i]
        return ans