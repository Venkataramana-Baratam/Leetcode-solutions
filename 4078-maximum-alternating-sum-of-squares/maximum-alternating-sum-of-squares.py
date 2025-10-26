class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        temp = sorted(abs(x) for x in nums)  # ✅ sort once — O(n log n)
        res = []

        # Build result by pairing largest and smallest
        while len(temp) >= 2:
            even_maxi = temp.pop()   # last element = max
            odd_mini = temp.pop(0)   # first element = min
            res.append(even_maxi)
            res.append(odd_mini)

        if len(temp) == 1:
            res.append(temp[0])

        even_sum = 0
        odd_sum = 0
        for i in range(len(res)):
            if i % 2 == 0:
                even_sum += res[i] ** 2
            else:
                odd_sum += res[i] ** 2

        return even_sum - odd_sum
