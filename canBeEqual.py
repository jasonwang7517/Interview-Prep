class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        dict = {}
        dict2 = {}
        for el in target:
            if el not in dict:
                dict[el] = 1
            else:
                dict[el] = dict[el] + 1
        for el2 in arr:
            if el2 not in dict2:
                dict2[el2] = 1
            else:
                dict2[el2] = dict2[el2] + 1
        for k in dict:
            if k not in dict2 or dict[k] != dict2[k]:
                return False
        return True
        