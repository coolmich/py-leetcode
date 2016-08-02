# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals, res = sorted(intervals, key=lambda x:x.start), []
        for interval in intervals:
            s, e = interval.start, interval.end
            if res and s <= res[-1][1]:
                res[-1][1] = max(res[-1][1], e)
            else:
                res.append([s,e])
        return [Interval(s=s, e=e) for [s, e] in res]