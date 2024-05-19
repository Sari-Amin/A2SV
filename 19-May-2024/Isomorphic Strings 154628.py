# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        res = set(zip(s,t))

        return len(res) == len(set(s)) == len(set(t))