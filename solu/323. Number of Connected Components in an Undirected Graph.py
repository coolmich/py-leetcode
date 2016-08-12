from collections import defaultdict
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        def visit(ed, u):
            if u in ed:
                to_v = ed[u]
                ed.pop(u)
                for v in to_v:
                    visit(ed, v)
        ed = defaultdict(list)
        for u, v in edges:
            ed[u].append(v)
            ed[v].append(u)
        sing, cnt = n - len(ed), 0
        while ed.keys():
            visit(ed, ed.keys()[0])
            cnt += 1
        return cnt + sing