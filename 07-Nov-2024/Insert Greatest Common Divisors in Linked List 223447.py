# Problem: Insert Greatest Common Divisors in Linked List - https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = head
        
        while ptr1.next:
            p = ptr1.val
            q = ptr1.next.val
            node = ListNode(gcd(p, q), ptr1.next)
            ptr1.next = node
            ptr1 = ptr1.next.next
        
        return head