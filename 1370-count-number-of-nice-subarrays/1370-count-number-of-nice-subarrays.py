class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def nice(S):
            l = 0
            r = 0
            n = len(nums)
            cnt =0
            odd_count = 0
            if S<0:
                return 0
            while r<n:
                if nums[r]%2!=0:
                    odd_count+=1
                while odd_count>S:
                    if nums[l]%2!=0:
                        odd_count-=1
                    l+=1
                cnt+=(r-l+1)
                r+=1
            return cnt
        return nice(k)-nice(k-1)

