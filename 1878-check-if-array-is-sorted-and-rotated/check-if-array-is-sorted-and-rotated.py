class Solution:
    def check(self, nums: List[int]) -> bool:
        

        ind = -1

        for i in range(len(nums) - 1):

            if nums[i] > nums[i+1]:
                ind = i
                break

        if ind == -1:
            return True
        
        rot = nums[:ind+1]
        rem = nums[ind+1:]

        new = rem + rot

        return all(new[i] <= new[i+1] for i in range(len(new)-1))