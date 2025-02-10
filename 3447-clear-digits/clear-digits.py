class Solution:
    def clearDigits(self, s: str) -> str:
        l1=[]
        for i in s:
            if i.isdigit() and l1:
                l1.pop()
            else:
                l1.append(i)
        return "".join(l1)