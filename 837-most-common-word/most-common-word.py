class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph = paragraph.lower()
        
        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, " ")
        
        words = paragraph.split()
        banned_set = set(banned)
        
        count = Counter()
        
        for word in words:
            if word not in banned_set:
                count[word] += 1
        
        return count.most_common(1)[0][0]