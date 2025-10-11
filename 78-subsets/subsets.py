class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        ds = []

        def printallsubsequence(i, ds, n):
            if i == n:
                ans.append(ds[:]) 
                return
            ds.append(nums[i])
            printallsubsequence(i + 1, ds, n)
            ds.pop()
            printallsubsequence(i + 1, ds, n)
        printallsubsequence(0, ds, n)
        return ans
