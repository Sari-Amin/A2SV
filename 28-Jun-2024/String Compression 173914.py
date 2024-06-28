# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) <= 1:
            return 1

        ans = 0
        cur = chars[0]
        count = 0
        ptr = 0
        for i in range(len(chars)):
            if cur == chars[i]:
                count += 1
            else:
                chars[ptr] = cur
                ptr += 1
                if count > 1:
                    temp = str(count)
                    for j in temp:
                        chars[ptr] = j
                        ptr += 1
                        ans += 1
                cur = chars[i]
                ans += 1
                count = 1
    
        chars[ptr] = cur
        ptr += 1
        if count > 1:
            temp = str(count)
            for j in temp:
                chars[ptr] = j
                ptr += 1
                ans += 1
        ans += 1

        return ans