# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
from collections import defaultdict
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        ret = 0
        for i in range(len(points)):
            mapi, maxi = defaultdict(int), 0
            x1, y1, same = points[i].x, points[i].y, 1
            for j in range(i+1, len(points)):
                x2, y2 = points[j].x, points[j].y
                if x1 == x2 and y1 == y2:
                    same += 1
                    continue
                if x1 == x2: k = 'inf'
                elif y1 == y2: k = '0'
                else: k = str((y1-y2)*1.0/(x1-x2))
                mapi[k] += 1
                maxi = max(maxi, mapi[k])
            ret = max(ret, maxi+same)
        return ret