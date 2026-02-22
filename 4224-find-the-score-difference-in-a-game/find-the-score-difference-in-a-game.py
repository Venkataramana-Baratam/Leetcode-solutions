class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        first = True
        n = len(nums)
        p1 =0
        p2 =0
        for i in range(n):


            if nums[i]%2==1:
                first = not first

            if (i+1)%6==0:
                first = not first
            
            if first:
                p1+=nums[i]
            else:
                p2+=nums[i]
        return p1 - p2