from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve(n):
            prime=[True]*(n+1)
            prime[0]=prime[1]=False
            for i in range(2,int(n**0.5)+1):
                if prime[i]:
                    for j in range(i*i,n+1,i):
                        prime[j]=False
            return [i for i in range(left,right+1) if prime[i]]
        k=sieve(right)

        if len(k)<2:
            return[-1,-1]
        res=[-1,-1]
        min_diff=float('inf')
        for num in range(len(k)-1):
            diff=k[num+1]-k[num]
            if diff<min_diff:
                min_diff=diff
                res=[k[num],k[num+1]]
        return res