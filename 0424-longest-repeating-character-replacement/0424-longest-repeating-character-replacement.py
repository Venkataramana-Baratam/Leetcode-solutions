class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r =0
        n =len(s)
        maxi_f = 0
        hash = [0]*26
        max_len =0
        while r<n:
            hash[ord(s[r])-ord('A')]+=1
            maxi_f = max(maxi_f,hash[ord(s[r])-ord('A')])
            if (r -l+1)-maxi_f>k:
                hash[ord(s[l])-ord('A')]-=1
                l+=1
                maxi_f = 0
            if (r - l +1)-maxi_f<=k:
                max_len = max(max_len,r-l+1)
            r+=1
        return max_len

