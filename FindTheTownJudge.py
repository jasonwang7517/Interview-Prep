"""
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
"""

from collections import defaultdict

class Solution(object):
    def findJudge(self, n, trust):
        trusts = defaultdict(list)
        trusted_by = defaultdict(list)
        for i in trust:
            trusts[i[0]].append(i[1])
            trusted_by[i[1]].append(i[0])
        for i in range(1, n + 1):
            if len(trusts[i]) == 0 and len(trusted_by[i]) == n - 1:
                return i
        return -1