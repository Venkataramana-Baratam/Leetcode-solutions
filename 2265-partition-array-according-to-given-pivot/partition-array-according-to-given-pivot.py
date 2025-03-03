class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lesser=[]
        greater=[]
        equal=[]
        for num in nums:
            if num==pivot:
                equal.append(num)
            elif(num<pivot):
                lesser.append(num)
            else:
                greater.append(num)
        l1 =lesser+equal+greater
        return l1