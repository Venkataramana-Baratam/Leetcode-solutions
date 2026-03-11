class Solution:
    def findComplement(self, num: int) -> int:
        

        bin_val = bin(num)[2::]
        c_bin = ['1' if x=='0' else '0' for x in str(bin_val)]
        res = ''.join(c_bin)       
        return int(res,2)