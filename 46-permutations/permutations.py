class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ds = []
        freq = [0]*n
        ans = []
        def f(ds,freq,ans):
            for i in range(n):
                if freq[i]==0:
                    ds.append(nums[i])
                    freq[i] = 1
                    f(ds,freq,ans)
                    freq[i] = 0
                    ds.pop()
            if len(ds) == n:
                ans.append(ds[:])
                return 
        f(ds,freq,ans)
        return ans
