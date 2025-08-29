class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x:x[0])
        n = len(intervals)
        i = 1
        res = [intervals[0]]
        while i<n:
            last = res[-1]
            if intervals[i][0]<=last[1]:
                last[1] = max(last[1],intervals[i][1])                
            else:
                res.append(intervals[i])
            i+=1
        return res