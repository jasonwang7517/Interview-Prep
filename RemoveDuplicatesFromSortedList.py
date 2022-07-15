"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class RemoveDuplicatesFromSortedList(object):
    def deleteDuplicates(self, head):
        if head is None:
            return head
        last = head
        current = last.next
        while current:
            if current.val != last.val:
                last.next = current
                last = current
            current = current.next
        last.next = None
        return head
        