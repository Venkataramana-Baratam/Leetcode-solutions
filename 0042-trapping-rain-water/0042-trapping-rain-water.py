class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefixmax = [0]*n
        prefixmax[0] = height[0]
        for i in range(1,n):
            prefixmax[i] = max(prefixmax[i-1],height[i])
        suffixmax = [0]*n
        suffixmax[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            suffixmax[i] = max(suffixmax[i+1],height[i])
        total= 0
        for i in range(n):
            leftmax = prefixmax[i]
            rightmax = suffixmax[i]
            if height[i]<leftmax and height[i]<rightmax:
                total += min(leftmax,rightmax)-height[i]
        return total