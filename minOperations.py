class Solution(object):
    def minOperations(self, logs):
        stack = []
        for i in logs:
            if i == "../" and len(stack) > 0:
                stack.pop()
            elif i != "./" and i != '../':
                stack.append(i)
        return len(stack)
