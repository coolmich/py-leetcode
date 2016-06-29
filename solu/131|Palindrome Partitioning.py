class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        mat = [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            mat[i][i] = True
        for i in range(len(s)-1):
            mat[i][i+1] = s[i] == s[i+1]
        for interval in range(2, len(s)):
            for start in range(len(s)-interval):
                mat[start][start+interval] = s[start] == s[start+interval] and mat[start+1][start+interval-1]
        return self.helper(s, mat, 0)

    def helper(self, s, mat, start):
        if start == len(s): return [[]]
        if start == len(s) - 1: return [[s[start]]]
        res = []
        for i in range(start, len(s)):
            if mat[start][i]:
                for arr in self.helper(s, mat, i+1):
                    res.append([s[start:i+1]] + arr)
        return res
                    