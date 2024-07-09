# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
     
        temp = head
        ans = head
        num = 0
        while temp:
            if temp.val != 0:
                num += temp.val
            else:
                if num != 0:
                    ans.next = ListNode(num)
                    num = 0
                    ans = ans.next
            temp = temp.next

        return head.next