class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def is_prime(num):
            if num<=1:
                return False
            for i in range(2,int(num**0.5)+1):
                if num%i == 0:
                    return False
            return True
        mpp = {}
        for i in nums:
            if i in mpp:
                mpp[i]+=1
            else:
                mpp[i] =1
        for key,value in mpp.items():
            if is_prime(value):
                return True
        return False
