class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        rows = len(queries)
        for i in range(rows):
            start = queries[i][0]
            end = queries[i][1]
            k_i = queries[i][2]
            v_i = queries[i][3]
            while start<=end:
                nums[start] = (nums[start]*v_i)%(10**9+7)
                start+=k_i
        res =0
        for i in range(len(nums)):
            res^=nums[i]
        return res