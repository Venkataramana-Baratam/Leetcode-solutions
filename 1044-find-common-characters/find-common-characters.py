class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])
        for word in words[1:]:
            common &= Counter(word)

        res = []
        for ch, cnt in common.items():
            res.extend([ch] * cnt)

        return res