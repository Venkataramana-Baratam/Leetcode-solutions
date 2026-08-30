class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        n = len(nums)

       # if n == 1:
#            return n

        max_ind = float('-inf')

        min_ind = float('inf')
        maxi = float('-inf')
        mini = float('inf')
        for i in range(n):

            if nums[i] > maxi:
                maxi = nums[i]
                max_ind = i
            if nums[i] < mini:
                mini = nums[i]
                min_ind = i
        
        n1 = min(min_ind + 1 , n - min_ind)
        n2 = min(max_ind + 1, n - max_ind)

        return min(n1 + n2, max(min_ind, max_ind)+1 , n - min(min_ind, max_ind))