from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            length = str(len(s)).zfill(3)
            ans = ans + length + s
        return ans

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            length = int(s[i:i+3])
            word = s[i+3:i+3+length]
            result.append(word)
            i = i + 3 + length
        return result