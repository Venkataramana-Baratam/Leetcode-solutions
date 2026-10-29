class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        bin_a = bin(a)[2::]
        bin_b =  bin(b)[2::]

        s1 = 0
        s2 = 0

        for ch in bin_a:
            if ch == '1':
                s1+=1
        for ch in bin_b:
            if ch == '1':
                s2+=1

        if s1 >= s2:
            return s1 * s2

        else:
            return s2 // s1