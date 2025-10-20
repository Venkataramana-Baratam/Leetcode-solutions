class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ds = []
        ans = []
        def f(i,ds,target):
            if i==n:
                if target==0:
                    ans.append(ds[:])
                return 
            if candidates[i]<=target:
                ds.append(candidates[i])
                f(i,ds,target-candidates[i])
                ds.pop()
            f(i+1,ds,target)
        f(0,ds,target)
        return ans
                    