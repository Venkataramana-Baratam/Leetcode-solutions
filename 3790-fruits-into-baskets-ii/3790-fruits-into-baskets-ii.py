class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        bools = [False]*len(fruits)
        cnt = 0
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if fruits[i]<=baskets[j] and bools[j]!=True:
                    bools[j] = True
                    cnt+=1
                    break
        return len(fruits)-cnt
        