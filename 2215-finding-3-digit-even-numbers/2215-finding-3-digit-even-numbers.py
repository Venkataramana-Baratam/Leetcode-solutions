class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        perm_list = permutations(digits,3)
        unique_list = set()
        for p in perm_list:
            if p[0]!=0:
                num = p[0]*100+p[1]*10+p[2]
                if num%2==0:
                    unique_list.add(num)
        return sorted(unique_list)