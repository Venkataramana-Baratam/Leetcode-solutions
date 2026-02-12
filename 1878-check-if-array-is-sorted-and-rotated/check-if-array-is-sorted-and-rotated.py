class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        ind = -1
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                ind = i
                break

        if ind == -1:
            return True

        inc = nums[:ind + 1]
        rem = nums[ind + 1:]
        res = rem + inc

        return all(res[i] <= res[i + 1] for i in range(n - 1))
