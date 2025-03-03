class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l1 = []
        l2=[]
        for num in nums:
            if num!=0:
                l1.append(num)
        for j in nums:
            if j ==0:
                l2.append(j)
        nums[:]=l1+l2