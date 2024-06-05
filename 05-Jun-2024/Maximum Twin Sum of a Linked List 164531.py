# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l = []
        curr = head
        ans = 0
        while curr:
            l.append(curr.val)
            curr = curr.next
        right = len(l)-1
        left = 0
        while left < right:
            ans = max(ans,l[left]+l[right])
            left += 1
            right -= 1
        return ans