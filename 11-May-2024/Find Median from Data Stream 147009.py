# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.numElements = 0

    def addNum(self, num: int) -> None:
        self.numElements += 1
        if self.numElements % 2:
            if self.min_heap and  num > self.min_heap[0]:
                temp = heappop(self.min_heap)
                heappush(self.min_heap, num)
                heappush(self.max_heap, -temp)
            else:
                heappush(self.max_heap, -num)
        else:
            if self.max_heap and  num < -self.max_heap[0]:
                temp = -heappop(self.max_heap)
                heappush(self.min_heap, temp)
                heappush(self.max_heap, -num)
            else:
                heappush(self.min_heap, num)

        

    def findMedian(self) -> float:
        if self.numElements % 2:
            return -self.max_heap[0]
        return (self.min_heap[0] + -self.max_heap[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()