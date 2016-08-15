from collections import defaultdict
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        mapa, mapb, res = defaultdict(list), defaultdict(list), [[0 for i in range(len(B[0]))] for j in range(len(A))]
        for r in range(len(A)):
            for c in range(len(A[0])):
                if A[r][c]: mapa[c].append(r)
        for r in range(len(B)):
            for c in range(len(B[0])):
                if B[r][c]: mapb[r].append(c)
        for i in range(len(A[0])):
            for ar in mapa[i]:
                for bc in mapb[i]:
                    res[ar][bc] += A[ar][i]*B[i][bc]
        return res
