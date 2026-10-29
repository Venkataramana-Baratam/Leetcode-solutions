class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        

        s1 = 0
        s2 = 0
        for i in range(1,len(nums)-1):

            if nums[i-1] < nums[i] > nums[i+1]:

                s1+=nums[i]

        for i in range(1,len(nums)-1):

            if nums[i-1] > nums[i] < nums[i+1]:
                s2 += nums[i]

        return s1 - s2