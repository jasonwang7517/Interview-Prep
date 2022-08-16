"""
You are given two 2D integer arrays, items1 and items2, representing two sets of items. Each array items has the following properties:
    - items[i] = [valuei, weighti] where valuei represents the value and weighti represents the weight of the ith item.
    - The value of each item in items is unique.

Return a 2D integer array ret where ret[i] = [valuei, weighti], with weighti being the sum of weights of all items with value valuei.

Note: ret should be returned in ascending order by value.
"""

from collections import defaultdict

class MergeSimilarItems(object):
    def mergeSimilarItems(self, items1, items2):
        items = defaultdict(lambda: 0)
        for i in items1:
            items[i[0]] += i[1]
        for i in items2:
            items[i[0]] += i[1]
        ans = []
        for i in items:
            curr = [i, items[i]]
            ans.append(curr)
        ans = sorted(ans, key=lambda x: x[0])
        return ans