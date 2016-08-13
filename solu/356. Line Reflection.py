from collections import defaultdict
class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        def axis(arr):
            cand, mapi = sum(arr)*1.0/len(arr), {}
            for item in arr:
                if item != cand:
                    if item in mapi: mapi.pop(item)
                    else:
                        ana = 2*cand-item
                        mapi[ana] = 1
            return (not len(mapi), cand)

        mapi, prev = defaultdict(list), None
        for x, y in points:
            if x not in mapi[y]: mapi[y].append(x)
        for y in mapi:
            tf, cand = axis(mapi[y])
            if not tf: return False
            if prev is None: prev = cand
            if prev != cand: return False
        return True