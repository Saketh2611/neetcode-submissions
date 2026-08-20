class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0 
        n = len(intervals)
        intervals.sort(key = lambda x : (x[1],x[0]))
        end = intervals[0][1]
        for i in range(1,n):
            if intervals[i][0] < end :
                count += 1 
            else : 
                end = intervals[i][1]
        return count
        