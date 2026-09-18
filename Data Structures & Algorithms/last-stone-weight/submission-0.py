import heapq

class Solution:
    def lastStoneWeight(self, stones):
        # Convert to negative numbers to create a max heap
        stones = [-stone for stone in stones]

        # Build the heap
        heapq.heapify(stones)

        while len(stones) > 1:
            # Get the two heaviest stones
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)

            # If they are different, put the remaining weight back
            if x != y:
                heapq.heappush(stones, -(x - y))

        # If one stone remains, return its weight
        if stones:
            return -stones[0]

        return 0