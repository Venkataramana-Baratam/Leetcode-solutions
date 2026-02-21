from collections import Counter

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
        
        cnt = 0
        
        for num in range(left, right + 1):
            bin_num = bin(num)[2:]
            counter = Counter(bin_num)

            for key, val in counter.items():
                if key == '1':        
                    if is_prime(val):
                        cnt += 1
        
        return cnt