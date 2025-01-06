# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = head
        visited = set()
        while ans:
            if ans not in visited:
                visited.add(ans)
                ans = ans.next
            else:
                return ans
        return ans