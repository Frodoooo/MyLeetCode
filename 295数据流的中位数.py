import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lo = []
        self.hi = []
        heapq.heapify(self.lo)
        heapq.heapify(self.hi)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, - heapq.heappop(self.lo))
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, - heapq.heappop(self.hi))


    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            return - self.lo[0]
        else:
            return  (- self.lo[0] + self.hi[0])/2


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())