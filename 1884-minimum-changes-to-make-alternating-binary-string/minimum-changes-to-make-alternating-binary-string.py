class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        A = [0]*n
        B = [0]*n
        if all(x==s[0] for x in s):
            
            return n//2
        for i in range(n):
            if i%2==0:
                A[i] = '0'
                B[i] = '1'
            else:
                A[i] = '1'
                B[i] = '0'
        c1 = 0
        c2 = 0
        for i in range(n):
            if A[i]!=s[i]:
                c1+=1
            if B[i]!=s[i]:
                c2+=1
        return min(c1,c2) 