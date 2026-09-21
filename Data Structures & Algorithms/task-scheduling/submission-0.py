class Solution:
    def leastInterval(self, tasks, n):
        
        freq = [0] * 26

        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        maxFreq = max(freq)

        maxCount = freq.count(maxFreq)

        result = (maxFreq - 1) * (n + 1) + maxCount

        return max(len(tasks), result)