"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class RemoveLinkedListElements(object):
    def removeElements(self, head, val):
        prev = None
        while head and head.val == val:
            head = head.next
        current = head
        while current:
            if current.val != val:
                prev = current
                current = current.next
            else:
                current = current.next
                prev.next = current
        return head
        
        