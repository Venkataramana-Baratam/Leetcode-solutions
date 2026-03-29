class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        
        n1 = len(s1)
        n2 = len(s2)

      
        if s1==s2:
            return True
        even = {}
        odd = {}

       
        for i, ch in enumerate(s1):
            if i % 2 == 0:
                even[ch] = i
            else:
                odd[ch] = i
        
        def even_swap(x):
            res = list(x)
            values = [v for v in even.values()]
            
            for i in range(len(values) - 1):
                res[values[i]], res[values[i+1]] = res[values[i+1]], res[values[i]]
            
            return "".join(res)

        def odd_swap(y):
            res = list(y)
            values = [v for v in odd.values()]
            
            
            for i in range(len(values) - 1):
                res[values[i]], res[values[i+1]] = res[values[i+1]], res[values[i]]
            
            return "".join(res)

        def both_swap():
            temp = even_swap(s1)
            temp = odd_swap(temp)
            return temp

        r1 = even_swap(s1)
        r2 = odd_swap(s1)
        r3 = both_swap()
        return (r1==s2) or (r2==s2) or (r3 ==s2)
