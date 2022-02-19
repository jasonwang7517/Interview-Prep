"""
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:
    - void push(int x) Pushes element x to the top of the stack.
    - int pop() Removes the element on the top of the stack and returns it.
    - int top() Returns the element on the top of the stack.
    - boolean empty() Returns true if the stack is empty, false otherwise.

Notes:
    - You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
    - Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

"""

class MyStack(object):

    q_push = []
    q_pop = []
    
    def __init__(self):
        self.q_push = []
        self.q_pop = []
        

    def push(self, x):
        self.q_push.append(x)
        

    def pop(self):
        while len(self.q_push) > 1:
            self.q_pop.append(self.q_push.pop(0))
        ans = self.q_push.pop(0) 
        while len(self.q_pop) > 0:
            self.q_push.append(self.q_pop.pop(0))
        return ans
        

    def top(self):
        while len(self.q_push) > 1:
            self.q_pop.append(self.q_push.pop(0))
        ans = self.q_push[0]
        self.q_pop.append(self.q_push.pop(0))
        while len(self.q_pop) > 0:
            self.q_push.append(self.q_pop.pop(0))
        return ans
        

    def empty(self):
        return len(self.q_push) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()