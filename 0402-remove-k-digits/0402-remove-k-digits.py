class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        for digit in num:
            while st and st[-1] > digit and k>0:
                st.pop()
                k-=1
            st.append(digit)
        while k>0:
            st.pop()
            k-=1
        res = ''
        res = ''.join(st).lstrip('0')
        return res  if res else '0'