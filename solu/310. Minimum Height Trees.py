from collections import defaultdict
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges: return [0]
        deg = defaultdict(set)
        for u, w in edges:
            deg[u].add(w)
            deg[w].add(u)
        while len(deg) > 2:
            to_rm = [k for k in deg if len(deg[k]) == 1]
            for k in to_rm:
                deg[deg[k].pop()].remove(k)
                del deg[k]
        return deg.keys()