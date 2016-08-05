# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals: return 0
        intervals = sorted(intervals, key=lambda x:x.start)
        h = []
        for interval in intervals:
            if h and h[0] <= interval.start:
                heapq.heappop(h)
            heapq.heappush(h, (interval.end))
        return len(h)