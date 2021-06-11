"""
    Given an array of unique integers salary where salary[i] is the salary of the employee i.

    Return the average salary of employees excluding the minimum and maximum salary.
"""

class AverageSalaryExcludingMinimumMaximumSalary(object):
    def average(self, salary):
        salary.sort()
        del salary[0]
        del salary[-1]
        return sum(salary) / float(len(salary))
        