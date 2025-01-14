# Problem: Find-the-prefix-common-array-of-two-arrays - https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        prefix = [0] * len(A)
        dic_a = {}
        dic_b = {}
        for i in range(len(A)):
            if i == 0:
                dic_a[A[i]] = 1
                dic_b[B[i]] = 1
                if A[i] == B[i]:
                    prefix[i] = 1
            else:
                dic_a[A[i]] = 1
                dic_b[B[i]] = 1
                if A[i] == B[i]:
                    prefix[i] += 1
                else:
                    if A[i] in dic_b:
                        prefix[i] += 1
                    if B[i] in dic_a:
                        prefix[i] += 1
            
        for i in range(1,len(prefix)):
            prefix[i] += prefix[i - 1]
        return prefix