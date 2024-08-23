# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if len(firstList) == 0 or len(secondList) == 0:
            return []
        ans = []
        left = 0
        right = 0
        while left < len(firstList) and right < len(secondList):
            if firstList[left][0] <= secondList[right][0]:
                temp = [secondList[right][0]]
                if firstList[left][1] >= secondList[right][1]:
                    temp.append(secondList[right][1])
                    right += 1
                else:
                    temp.append(firstList[left][1])
                    left += 1
                if temp[0] <= temp[1]:
                    ans.append(temp)

            else:
                temp = [firstList[left][0]]
                if firstList[left][1] >= secondList[right][1]:
                    temp.append(secondList[right][1])
                    right += 1
                else:
                    temp.append(firstList[left][1])
                    left += 1
                if temp[0] <= temp[1]:
                    ans.append(temp)

        return ans



            