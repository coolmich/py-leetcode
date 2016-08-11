from collections import deque
class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        if not image or not image[0]: return 0
        q = deque([(x, y)])
        rmin = cmin = 2**31
        rmax = cmax = -1
        while q:
            r, c = q.popleft()
            if image[r][c] == '0':continue
            image[r][c] = '0'
            rmin, rmax, cmin, cmax = min(rmin, r), max(rmax, r), min(c, cmin), max(c, cmax)
            for rd, cd in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                r_, c_ = r+rd, c+cd
                if 0<=r_<len(image) and 0<=c_<len(image[0]) and image[r_][c_] == '1':
                    q.append((r_,c_))
        return (cmax-cmin+1)*(rmax-rmin+1)