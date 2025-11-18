class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        r = 0
        n = len(bits)
        while r < n-1:
            if bits[r] ==1:
                r+=2
            else:
                r+=1
        return r==n-1

