class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []

        def backtrack(start, current, total):
            if total == target:
                result.append(current[:])
                return

            if total > target:
                return

            for i in range(start, len(candidates)):

                # Duplicate combination avoid karo
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                current.append(candidates[i])

                # i + 1 because same element dobara use nahi kar sakte
                backtrack(i + 1, current, total + candidates[i])

                current.pop()

        backtrack(0, [], 0)
        return result
        