class Solution(object):
    def average(self, salary):
        salary.sort()
        del salary[0]
        del salary[-1]
        return sum(salary) / float(len(salary))
        