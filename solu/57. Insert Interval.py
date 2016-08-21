# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        s_, e_, res, i = newInterval.start, newInterval.end, [], 0
        while i < len(intervals):
            s, e = intervals[i].start, intervals[i].end
            if e < s_:
                res.append(intervals[i])
                i+=1
            else: break
        if i == len(intervals): return res + [newInterval]
        new_s = min(s, s_)
        while i < len(intervals) and e_ > intervals[i].end: i+=1
        if i == len(intervals) or e_ < intervals[i].start: new_e = e_
        else: new_e, i = intervals[i].end, i+1
        res.append(Interval(new_s, new_e))
        res += intervals[i:]
        return res
            