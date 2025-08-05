class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        cnt = 0
        l = 0
        r =0
        n =len(weight)
        maxi = 0
        while l<n:
            r = l 
            max_val = weight[l]
            while r<n:
                max_val = max(max_val,weight[r])
                if r>l and weight[r]<max_val:
                    cnt+=1
                    break
                r+=1
            l = r+1
        return cnt