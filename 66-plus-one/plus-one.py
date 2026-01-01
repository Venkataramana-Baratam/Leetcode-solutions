class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        s = ''
        for num in digits:
            s+=str(num)
        res = int(s) + 1
        ans = str(res)
        x  = []
        for i in ans:
            x.append(int(i))
        return x
