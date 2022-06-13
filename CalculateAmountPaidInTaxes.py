"""
You are given a 0-indexed 2D integer array brackets where brackets[i] = [upperi, percenti] means that the ith tax bracket has an upper bound of upperi and is taxed at a rate of percenti. 
The brackets are sorted by upper bound (i.e. upperi-1 < upperi for 0 < i < brackets.length).

Tax is calculated as follows:
    - The first upper0 dollars earned are taxed at a rate of percent0.
    - The next upper1 - upper0 dollars earned are taxed at a rate of percent1.
    - The next upper2 - upper1 dollars earned are taxed at a rate of percent2.
    - And so on.

You are given an integer income representing the amount of money you earned. Return the amount of money that you have to pay in taxes. Answers within 10-5 of the actual answer will be accepted.
"""

class CalculateAmountPaidInTaxes(object):
    def calculateTax(self, brackets, income):
        index = 0
        taxes = 0
        last_bracket = 0
        while income > 0:
            amount_taxed = min(income, brackets[index][0] - last_bracket)
            last_bracket = brackets[index][0]
            taxes_due = amount_taxed * (brackets[index][1] / 100.0)
            taxes += taxes_due
            income -= amount_taxed
            index += 1
        return taxes
        