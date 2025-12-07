N = 500005
p = [True] * N

def pre():
    p[0] = False
    p[1] = False

    i = 2
    while i * i < N:
        if p[i]:
            j = i * i
            while j < N:
                p[j] = False
                j += i
        i += 1


class Solution:
    def largestPrime(self, n: int) -> int:
        # Run sieve only once
        if p[0]:        # initially p[0] is True
            pre()       # after this, p[0] becomes False → no more calls

        total_sum = 0
        ans = 0

        for i in range(n + 1):
            if p[i]:
                total_sum += i

            if total_sum <= n and p[total_sum]:
                ans = total_sum

        return ans
