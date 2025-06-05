class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:       
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
            
        parent = list(range(26))
        for a, b in zip(s1, s2):
            x, y = ord(a) - 97, ord(b) - 97
            rx, ry = find(x), find(y)
            if rx != ry:
                if rx < ry:
                    parent[ry] = rx
                else:
                    parent[rx] = ry
        
        return ''.join(chr(find(ord(c) - 97) + 97) for c in baseStr)
