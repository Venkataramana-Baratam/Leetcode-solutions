class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        
        str_num = str(n)
        if (str(x) in str_num) and (str_num[0]!=str(x)):
            return True
        return False
