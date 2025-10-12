class Solution:
    def scoreBalance(self, s: str) -> bool:
        total = 0
        left_sum = 0
        right_sum = 0
        n = len(s)
        for i in s:
            total += ord(i) - ord('a')+1
        for i in range(n-1,-1,-1):
            left_sum += ord(s[i])-ord('a')+1
            right_sum = total - left_sum
            if left_sum==right_sum:
                return True
        return False