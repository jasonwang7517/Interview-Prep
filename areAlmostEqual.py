class Solution(object):
    def areAlmostEqual(self, s1, s2):
        if s1 == s2:
            return True
        diffs = []
        for i in range(0, len(s1)):
            if s1[i] != s2[i]:
                diffs.append(i)
        if len(diffs) > 2:
            return False
        return len(diffs) == 0 or (len(diffs) == 2 and s1[diffs[0]] == s2[diffs[1]] and s1[diffs[1]] == s2[diffs[0]])