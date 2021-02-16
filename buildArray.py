class buildArray(object):
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
        