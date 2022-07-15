"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
"""

class BackspaceStringCompare(object):
    def backspaceCompare(self, s, t):
        s_stack = []
        for i in s:
            if i == '#':
                if len(s_stack) > 0:
                    s_stack.pop()
            else:
                s_stack.append(i)
        t_stack = []
        for i in t:
            if i == '#':
                if len(t_stack) > 0:
                    t_stack.pop()
            else:
                t_stack.append(i)
        return t_stack == s_stack
        