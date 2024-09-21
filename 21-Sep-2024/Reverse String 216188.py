# Problem: Reverse String - https://leetcode.com/problems/reverse-string/description/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(l, r):
            if l >= r:
                return 
            s[l], s[r] = s[r], s[l]
            return reverse(l + 1, r - 1)

        r = len(s) - 1
        l = 0
        reverse(l, r)
     