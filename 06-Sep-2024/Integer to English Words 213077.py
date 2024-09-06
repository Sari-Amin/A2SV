# Problem: Integer to English Words - https://leetcode.com/problems/integer-to-english-words/

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        suffixes = ["", "Thousand", "Million", "Billion", "Trillion", "Quadrillion", "Quintillion", "Sextillion", "Septillion", "Octillion", "Nonillion", "Decillion"]
        words = []
        i = 0
        while num > 0:
            triplet = num % 1000
            num = num // 1000
            if triplet == 0:
                i += 1
                continue
            curr = []
            if triplet // 100 > 0:
                curr.append(ones[triplet // 100])
                curr.append("Hundred")
            if triplet % 100 >= 10 and triplet % 100 <= 19:
                curr.append(teens[triplet % 10])
            else:
                if triplet % 100 >= 20:
                    curr.append(tens[triplet % 100 // 10])
                if triplet % 10 > 0:
                    curr.append(ones[triplet % 10])
            if i > 0:
                curr.append(suffixes[i])
            words = curr + words
            i += 1
        return " ".join(words)