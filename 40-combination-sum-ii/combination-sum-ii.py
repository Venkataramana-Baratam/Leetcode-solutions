class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()        
        n = len(candidates)
        ds = []
        ans = []
        def f(i, ds, target):
            if target == 0:
                ans.append(ds[:])
                return
            if i == n:
                return

            for j in range(i, n):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if candidates[j] > target:
                    break

                ds.append(candidates[j])
                f(j + 1, ds, target - candidates[j])   
                ds.pop()

        f(0, ds, target)
        return ans
