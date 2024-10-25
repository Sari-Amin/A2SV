# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
   def furthestBuilding(self, h: List[int], b: int, l: int) -> int:
       p = []
       
       i = 0
       for i in range(len(h) - 1):
           difference = h[i + 1] - h[i]
           
           if difference <= 0:
               continue
           
           b -= difference
           heappush(p, -difference)
      
           if b < 0:
               b += -heappop(p)
               l -= 1
               
           if l < 0:
               return i
               
       return len(h)-1
  
