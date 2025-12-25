class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        
        capacity.sort(reverse = True)
        total = sum(apple)
        i= 0
        n = len(capacity)
        cnt = 0
        while i<n:
            cap = capacity[i]
            if total>0:
                total-=cap
                cnt+=1
            i+=1
        return cnt
