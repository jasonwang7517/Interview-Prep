"""
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:
    - void push(int x) Pushes element x to the back of the queue.
    - int pop() Removes the element from the front of the queue and returns it.
    - int peek() Returns the element at the front of the queue.
    - boolean empty() Returns true if the queue is empty, false otherwise.

Notes:
    - You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
    - Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's 
    standard operations.
"""

class MyQueue(object):
    stack_in = []

    def __init__(self):
        self.stack_in = []
        
    def push(self, x):
        self.stack_in.append(x)

    def pop(self):
        if self.stack_in:
            return self.stack_in.pop(0)
        
    def peek(self):
        if self.stack_in:
            return self.stack_in[0]

    def empty(self):
        return len(self.stack_in) == 0