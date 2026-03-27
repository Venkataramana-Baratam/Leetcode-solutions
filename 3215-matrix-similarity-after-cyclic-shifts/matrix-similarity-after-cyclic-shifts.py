class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        
        def left_shift(arr):
            first = arr[0]
            res = arr[1:]
            res.append(first)
            return res
            
        def right_shift(arr):
            last = arr[-1]
            res = arr[:len(arr)-1]
            return [last] + res
        
        
        temp = [row[:] for row in mat]

        m = len(mat)

        for i in range(m):
            for _ in range(k):
                if i % 2 == 0:   
                    temp[i] = left_shift(temp[i])
                else:            
                    temp[i] = right_shift(temp[i])

        return temp == mat