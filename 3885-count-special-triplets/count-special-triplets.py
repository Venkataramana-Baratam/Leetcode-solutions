class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        freq = {}

        for i in nums:
            freq[i] = freq.get(i,0)+1
        freq_partial = {}
        cnt = 0
        for v in nums:

            target = v*2
            l_cnt = freq_partial.get(target,0)
            freq_partial[v] = freq_partial.get(v,0)+1
            r_cnt = freq.get(target,0) - freq_partial.get(target,0)
            cnt = ( cnt+l_cnt*r_cnt) %(10**9+7)
        return cnt