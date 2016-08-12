from collections import defaultdict
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        def dfs(u, pre, ed):
            for v in ed[u]:
                if v != pre[u]:
                    if v in pre: return False
                    pre[v] = u
                    if not dfs(v, pre, ed): return False
            return True
        ed, pre = defaultdict(list), {}
        for u, v in edges:
            ed[u].append(v)
            ed[v].append(u)
        u = None
        for u in ed:
            if len(ed[u]) == 1: break
        if u is None: return n <= 1
        pre[u] = u
        if not dfs(u, pre, ed): return False
        return len(pre) == n