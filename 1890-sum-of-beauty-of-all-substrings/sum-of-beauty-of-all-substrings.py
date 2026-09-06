class Solution:
    def beautySum(self, s: str) -> int:
        
        n = len(s)
        total = 0
        for i in range(n):
            freq = {}
            for j in range(i,n):
                
                freq[s[j]] = freq.get(s[j],0)+1


                values = freq.values()

                maxi = max(values)
                mini = min(values)

                total +=maxi - mini


        return total
