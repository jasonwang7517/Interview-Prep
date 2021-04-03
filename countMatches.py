class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        ans = 0
        key = 0
        if ruleKey == "color":
            key = 1
        elif ruleKey == "name":
            key = 2
        for item in items:
            if item[key] == ruleValue:
                ans += 1
        return ans