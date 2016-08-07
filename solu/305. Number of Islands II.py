class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        uf, stack = UF(), []
        for row, col in positions:
            p1 = (row,col)
            uf.add(p1, (row,col))
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                r, c = row+x, col+y
                if (r,c) in uf.ans:
                    p2 = uf.find((r,c))
                    if p1 != p2: p1 = uf.merge(p1, p2)
            stack.append(uf.cnt)
        return stack
        
class UF(object):
    def __init__(self):
        self.ans = {}
        self.sz = {}
        self.cnt = 0
    
    def add(self, ancestor, child):
        self.ans[child] = ancestor
        self.sz[ancestor] = 1
        self.cnt += 1
    
    def find(self, child):
        if child not in self.ans: return child
        while self.ans[child] != child:
            self.ans[child] = self.ans[self.ans[child]]
            child = self.ans[child]
        return child
    
    def merge(self, p1, p2):
        p1, p2 = (p1, p2) if self.sz[p1] > self.sz[p2] else (p2, p1)
        self.ans[p2] = p1
        self.sz[p1] += self.sz[p2]
        self.sz.pop(p2)
        self.cnt -= 1
        return p1
