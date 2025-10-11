class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  
        n = len(nums)
        ds = []
        ans = set()  

        def printallsubsequence(i, ds, n):
            if i == n:
                ans.add(tuple(ds)) 
                return
            ds.append(nums[i])
            printallsubsequence(i + 1, ds, n)
            ds.pop()
            printallsubsequence(i + 1, ds, n)

        printallsubsequence(0, ds, n)
        return [list(t) for t in ans]
