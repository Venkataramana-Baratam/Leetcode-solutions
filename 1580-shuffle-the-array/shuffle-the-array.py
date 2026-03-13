class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr1 = nums[:n]
        arr2 = nums[n:]
        
        res = []
        for i in range(n):
            res.append(arr1[i])
            res.append(arr2[i])
            
        return res