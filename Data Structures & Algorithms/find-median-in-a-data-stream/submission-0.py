import heapq

class MedianFinder:

    def __init__(self):
        # Max heap for the smaller half
        self.left = []

        # Min heap for the larger half
        self.right = []

    def addNum(self, num):
        # Add to max heap
        heapq.heappush(self.left, -num)

        # Make sure every element in left <= every element in right
        if self.left and self.right and (-self.left[0] > self.right[0]):
            value = -heapq.heappop(self.left)
            heapq.heappush(self.right, value)

        # Balance the sizes
        if len(self.left) > len(self.right) + 1:
            value = -heapq.heappop(self.left)
            heapq.heappush(self.right, value)

        elif len(self.right) > len(self.left):
            value = heapq.heappop(self.right)
            heapq.heappush(self.left, -value)

    def findMedian(self):
        if len(self.left) > len(self.right):
            return float(-self.left[0])

        return (-self.left[0] + self.right[0]) / 2.0
        