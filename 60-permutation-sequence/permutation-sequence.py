class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = 1
        numbers = []

        for i in range(1, n):
            fact *= i
            numbers.append(i)
        numbers.append(n)
        ans = ""
        k -= 1  

        while True:
            index = k // fact
            ans += str(numbers[index])
            numbers.pop(index)

            if not numbers:
                break

            k %= fact
            fact //= len(numbers)

        return ans
