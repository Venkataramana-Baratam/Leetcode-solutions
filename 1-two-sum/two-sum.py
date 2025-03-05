class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mpp={}
        for i in range(len(nums)):
            k =nums[i]
            moreneeded=target-k
            if moreneeded in mpp:
                return [mpp[moreneeded],i]
            mpp[k]=i
        return []