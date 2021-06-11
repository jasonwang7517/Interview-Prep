"""
   Given two integer arrays of equal length target and arr.

    In one step, you can select any non-empty sub-array of arr and reverse it. You are allowed to make any number of steps.

    Return True if you can make arr equal to target, or False otherwise. 
"""

class MakeTwoArraysEqual(object):
    def canBeEqual(self, target, arr):
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
        