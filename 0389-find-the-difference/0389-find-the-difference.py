class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter1 = Counter(s)
        counter2 = Counter(t)
        for char in counter2:
            if counter2[char]!=counter1.get(char,0):
                return char