class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)  # 🔑 SORTING
        
        n = len(intervals)
        if n == 0:
            return True
        
        finish = intervals[0].end
        for i in range(1, n):
            if intervals[i].start < finish:
                return False
            finish = intervals[i].end
        
        return True
