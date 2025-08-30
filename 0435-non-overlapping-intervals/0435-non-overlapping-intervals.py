class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        i =1
        cnt = 1
        last = intervals[0]
        n = len(intervals)
        print(intervals)
        while i<n:
            if last[1]<=intervals[i][0]:
                cnt+=1
                last = intervals[i]
            i+=1
        return n - cnt