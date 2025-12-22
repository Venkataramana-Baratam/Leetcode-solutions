class Solution:
    def completePrime(self, num: int) -> bool:
        prefix = []
        suffix = []
        st = str(num)
        pre = ""
        for i in range(len(st)):
            pre += st[i]
            prefix.append(int(pre))
        suf = ""
        for i in range(len(st) - 1, -1, -1):
            suf = st[i] + suf     
            suffix.append(int(suf))

        def prime(arr):
            for num in arr:

                if num<=1:
                    return False
                for i in range(2,int(num**0.5)+1):
                    if num % i ==0:
                        return False
            return True
        
        b1 = prime(prefix)
        b2 = prime(suffix)
        return b1 and b2 
