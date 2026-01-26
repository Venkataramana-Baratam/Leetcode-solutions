class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        

        n = len(nums)
        pos = []
        for i in range(n):
            if nums[i]>=0:
                pos.append(nums[i])
        m = len(pos)
        if len(pos)==0:
            return nums
        k = k%m
        pos = pos[k:]+pos[:k]
        j = 0
        for i in range(n):
            if nums[i]>=0:
                nums[i] = pos[j]
                j+=1
        return nums