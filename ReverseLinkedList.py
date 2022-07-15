"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

class ReverseLinkedList(object):
    def reverseList(self, head):
        prev = None
        curr = head
        while (curr is not None):
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev

class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next