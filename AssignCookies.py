"""
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], 
we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.
"""

class AssignCookies(object):
    def findContentChildren(self, g, s):
        ans = 0
        g.sort()
        s.sort()
        g_pointer = 0
        s_pointer = 0
        ans = 0
        while g_pointer < len(g) and s_pointer < len(s):
            if g[g_pointer] <= s[s_pointer]:
                ans += 1
                g_pointer += 1
                s_pointer += 1
            else:
                s_pointer += 1
        return ans
        