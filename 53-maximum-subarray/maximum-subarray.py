import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        maxi = -sys.maxsize-1
        start=-1
        end=-1
        tempstart=-1 
        for i in range(len(nums)):
            sum+=nums[i]
            if sum>maxi:
                maxi=sum
                start=tempstart
                end=i
            if sum<0:
                sum=0
                tempstart=i+1
        print(nums[start:end+1])
        return maxi