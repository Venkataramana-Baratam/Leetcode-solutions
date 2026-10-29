class Solution:
    def hammingWeight(self, n: int) -> int:
        

        one_bits = bin(n)[2::]

        s1 = 0

        for ch in one_bits:

            if ch == '1':
                s1+=1

        return s1