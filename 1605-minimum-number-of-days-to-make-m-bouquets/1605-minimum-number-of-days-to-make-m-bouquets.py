class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def possible(bloomDay,day,m,k):
            cnt=0
            nbk =0
            for i in range(len(bloomDay)):
                if bloomDay[i]<=day:
                    cnt+=1
                else:
                    nbk+=(cnt//k)
                    cnt=0
            nbk+=(cnt//k)
            if nbk>=m:
                return True
            else:
                False
        low = min(bloomDay)
        high = max(bloomDay)
        while low<=high:
            mid =(low+high)//2
            if len(bloomDay)<m*k:
                return -1
            if possible(bloomDay,mid,m,k)==True:
                high = mid-1
            else:
                low = mid+1
        return low
                