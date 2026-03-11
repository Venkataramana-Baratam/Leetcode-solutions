class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        bin_val = bin(n)[2::]
        st = str(bin_val)

        c_bin_val = ['1' if x=='0' else '0' for x in st]
        res = "".join(c_bin_val)
        
        return int(res,2)