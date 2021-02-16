class shortestToChar(object):
    def shortestToChar(self, s, c):
        occ = []
        ans = [0] * len(s)
        for i in range(0, len(s)):
            if s[i] == c:
                occ.append(i)
        if len(occ) == 1:
            for i in range(0, len(ans)):
                ans[i] = abs(occ[0] - i)
        else:
            left = 0
            right = 1
            i = 0
            while right < len(occ) and i < len(s):
                ans[i] = min(abs(occ[left] - i), abs(occ[right] - i))
                if abs(occ[right] - i) < abs(occ[left] - i):
                    left += 1
                    right += 1
                i += 1
            while i < len(s):
                ans[i] = abs(occ[left] - i)
                i += 1
        return ans