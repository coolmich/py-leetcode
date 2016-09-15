class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        seti, area = set(), 0
        for a, b, c, d in rectangles:
            area += (c-a)*(d-b)
            for x in (a,c):
                for y in (b,d):
                    if (x,y) in seti: seti.discard((x,y))
                    else: seti.add((x,y))
        if len(seti) != 4: return False
        pts = sorted(list(seti), key=lambda x: (x[0], x[1]))
        return area == (pts[-1][1] - pts[0][1]) * (pts[-1][0] - pts[0][0])