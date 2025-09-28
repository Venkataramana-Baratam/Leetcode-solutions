class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        str_n = str(n)
        n = len(str_n)
        k = 0
        res = []
        i = n-1
        while k<n:
            value = int(str_n[i])*10**k
            if value!=0:
                res.append(value)
            i-=1
            k+=1
        res.sort(reverse = True)
        return res
