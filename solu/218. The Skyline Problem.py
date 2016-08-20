import heapq
from collections import OrderedDict
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        pts, heap, to_rm, ret = [], [], {}, OrderedDict()
        prev = now = -1
        for idx,item in enumerate(buildings):
            s, e, h = item
            pts.append((s, -h, idx))
            pts.append((e, h, idx))
        for item in sorted(pts, key=lambda x:x[0]):
            n, h, idx = item
            if h < 0:
                heapq.heappush(heap, (h, idx))
            else:
                to_rm[idx] = 1
                while heap and heap[0][1] in to_rm:
                    to_rm.pop(heap[0][1])
                    heapq.heappop(heap)
            prev, now = now, -heap[0][0] if heap else 0
            if prev != now: ret[n] = now
        res = []
        for k in ret:
            if res and res[-1][1] == ret[k]: continue
            res.append([k, ret[k]])
        return res
