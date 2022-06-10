"""
Given the head of a singly linked list, return true if it is a palindrome.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class PalindromeLinkedList(object):
    def isPalindrome(self, head):
        ans = []
        current = head
        while current:
            ans.append(str(current.val))
            current = current.next
        if len(ans) == 1:
            return True
        s = ''.join(ans)
        first_half = s[:len(s) // 2]
        second_half = s[(len(s) // 2):][::-1]
        if len(second_half) > len(first_half):
            second_half = second_half[:-1]
        return first_half == second_half
        