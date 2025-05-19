class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        last = float('-inf')
        cnt=0
        longest =1
        if not nums:
            return 0
        for i in range(len(nums)):
            if nums[i]-1==last:
                cnt+=1
                last = nums[i]
            elif(nums[i]!=last):
                cnt=1
                last = nums[i]
            longest = max(longest,cnt)
        return longest