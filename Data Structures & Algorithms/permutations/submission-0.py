class Solution:
    def permute(self, nums):
        result = []

        def backtrack(current):
            if len(current) == len(nums):
                result.append(current[:])
                return

            for num in nums:
                if num in current:
                    continue

                current.append(num)
                backtrack(current)
                current.pop()

        backtrack([])
        return result
        