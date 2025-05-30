class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def allocate(nums,sum):
            req =1
            no_of_required =0
            for i in range(n):
                if no_of_required+nums[i]<=sum:
                    no_of_required+=nums[i]
                else:
                    req+=1
                    no_of_required=nums[i]
            return req
        low = max(nums)
        high = sum(nums)
        while low<=high:
            mid =(low+high)//2
            ans = allocate(nums,mid)
            if ans>k:
                low = mid+1
            else:
                high = mid-1
        return low
