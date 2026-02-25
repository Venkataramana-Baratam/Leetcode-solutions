class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        res = []

        for i in range(len(arr)):
            ones_cnt = bin(arr[i]).count('1')
            res.append([arr[i],ones_cnt])
        
        res.sort(key = lambda x:(x[1],x[0]))

        return [x[0] for x in res]
        