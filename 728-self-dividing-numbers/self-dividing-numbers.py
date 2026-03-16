class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        res  = []
        def divisible(num):
            for i in str(num):
                digit = int(i)
                if digit == 0 or num % digit != 0:
                    return False
            return True 
        for num in range(left,right+1):
            if divisible(num):
                res.append(num)
        return res