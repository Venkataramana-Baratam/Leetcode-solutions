from collections import Counter

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_count = Counter(s)
        t_count = Counter(target)

        ans = float('inf')

        for ch in t_count:
            ans = min(ans, s_count[ch] // t_count[ch])

        return ans