# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        ind = {}
        for i in range(len(s)):
            ind[s[i]] = i

        stack = []
        used = set() 
        for i in range(len(s)):

            if s[i] in used:
                continue

            while stack and stack[-1] > s[i] and ind[stack[-1]] > i :
                used.remove(stack[-1]) 
                stack.pop() 
                
            if s[i] not in used:
                stack.append(s[i])
                used.add(s[i])
        
        return ''.join(stack)