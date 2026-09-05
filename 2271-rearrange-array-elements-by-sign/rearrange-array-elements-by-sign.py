class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        

        pos = []
        neg = []
        for num in nums:

            if num < 0:
                neg.append(num)

            else:
                pos.append(num)
        n = len(nums)
        for i in range(len(pos)):
            nums[2*i] = pos[i]
        
        for j in range(len(neg)):
            nums[2 * j + 1]  = neg[j]

        return nums