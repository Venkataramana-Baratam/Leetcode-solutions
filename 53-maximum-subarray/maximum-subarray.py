class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        maxi = float('-inf')
        start=-1
        end=-1
        tempstart=-1 
        for i in range(len(nums)):
            
            if sum == 0:
                tempstart = i
            sum+=nums[i]

            if sum>maxi:
                maxi=sum
                start=tempstart
                end=i
            if sum<0:
                sum=0
        print(nums[start:end+1])
        return maxi