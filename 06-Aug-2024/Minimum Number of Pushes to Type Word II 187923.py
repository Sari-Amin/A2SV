# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        chars = sorted(set(word), reverse = True, key = lambda x: freq[x])
        ans = 0
        curr = 0
        mul = 1
        for i in range(len(chars)):
            curr += 1
            ans += freq[chars[i]] * mul
            if curr == 8:
                curr = 0
                mul += 1

        return ans