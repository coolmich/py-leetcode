class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        # write your code here
        if s == "": return True
        dict = set(wordDict)
        matrix = [[0 for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            if s[i:i+1] in dict:
                matrix[i][i] = 1
        diff = 1
        while diff < len(s):
            for col in range(diff, len(s)):
                row = col - diff
                if s[row:col+1] in dict:
                    matrix[row][col] = 1
                    continue
                for midPoint in range(row, col):
                    if matrix[row][midPoint]*matrix[midPoint+1][col] == 1:
                        matrix[row][col] = 1
            diff += 1
        return matrix[0][-1] == 1
        