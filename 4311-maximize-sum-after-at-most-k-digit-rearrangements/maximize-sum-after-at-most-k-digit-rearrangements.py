class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        def rearrange(n):
            str_of_n = str(n)
            ans = []
            for ch in str_of_n:
                ans.append(ch)
            ans.sort(reverse=True)
            return int(''.join(ans))

        transformed = []
        for num in nums:
            new_num = rearrange(num)
            transformed.append(new_num)

        diff = []
        for i in range(len(nums)):
            diff.append((transformed[i] - nums[i], i))

        diff.sort(reverse=True)

        total = sum(nums)

        for i in range(k):
            increase, idx = diff[i]
            if increase > 0:
                total += increase

        return total