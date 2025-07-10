class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack =[]
        res = [-1]*n
        for i in range(2*n-1,-1,-1):
            while stack and stack[-1]<=nums[i%n]:
                stack.pop()
            if len(stack)==0:
                res[i%n] = -1
            else:
                res[i%n] = stack[-1]
            stack.append(nums[i%n])
        return res