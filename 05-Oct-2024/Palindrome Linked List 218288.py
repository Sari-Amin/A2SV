# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        reverse = None
        while fast and fast.next:
            temp = slow
            fast = fast.next.next
            slow = slow.next

            temp.next = reverse
            reverse = temp
        
        if fast:
            slow = slow.next

        while slow:
            if slow.val != reverse.val:
                return False

            slow = slow.next
            reverse = reverse.next


        return True