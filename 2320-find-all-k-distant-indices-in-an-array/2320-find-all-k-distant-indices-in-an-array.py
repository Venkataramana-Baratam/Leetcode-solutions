class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        temp = []
        for i in range(len(nums)):
            if nums[i] == key:
                temp.append(i)
        res = []
        for j in range(len(nums)):
            for l in temp:
                if abs(j-l) <= k:
                    res.append(j)
        res = list(set(res))
        return res




