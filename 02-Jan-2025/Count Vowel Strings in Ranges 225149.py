# Problem: Count Vowel Strings in Ranges - https://leetcode.com/problems/count-vowel-strings-in-ranges/

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefixSum = [0]
        for i in range(len(words)):
            if (words[i][0] in "aeiou" and words[i][-1] in "aeiou"):
                prefixSum.append(prefixSum[-1] + 1)
            else:
                prefixSum.append(prefixSum[-1])

        ans = []
        
        for l, r in queries:
            temp = prefixSum[r + 1]
            if l != 0:
                temp -= prefixSum[l]
    
            ans.append(temp)

        return ans