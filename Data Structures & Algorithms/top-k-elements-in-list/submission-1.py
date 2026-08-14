class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for num in nums:
            if num not in count:
                count[num] = 0

            count[num] += 1

        sorted_count = sorted(count, key=count.get, reverse=True)

        return sorted_count[:k]