class Solution:
    def countElements(self, nums: List[int]) -> int:
        mini = float('inf')
        maxi = -float('inf')
        count =0 
        for num in nums:
            mini = min(mini,num)
            maxi = max(maxi,num)
        for num in nums:
            if num>mini and  num<maxi:
                count+=1
        return count