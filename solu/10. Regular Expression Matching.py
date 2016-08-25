class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def helper(s, sidx, p, pidx):
            if pidx == len(p):
                return sidx == len(s) or p[-1] == '*'
            if sidx == len(s):
                if p[pidx] == '*': return helper(s, sidx, p, pidx+1)
                else: return False
            if p[pidx] != '*':
                if p[pidx] == s[sidx] or p[pidx] == '?': return helper(s, sidx+1, p, pidx+1)
                return False
            else:
                i = sidx
                while i < len(s):
                    if helper(s, i, p, pidx+1): return True
                    i += 1
                return False
        if not s or not p: return False
        return helper(s, 0, p, 0)

        # dp = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        # dp[0][0] = True
        # for i in range(len(p)):
        #     if p[i] == '*': dp[0][i+1] = True
        #     else: break
        # for i in range(len(s)):
        #     for j in range(len(p)):
        #         if p[j] == '*': res = dp[i][j+1] or dp[i+1][j]
        #         elif p[j] == '?': res = dp[i][j]
        #         else: res = (s[i] == p[j] and dp[i][j])
        #         dp[i+1][j+1] = res
        # return dp[-1][-1]

print Solution().isMatch("bbbaaabaababbabbbaabababbbabababaabbaababbbabbbabb",
"*b**b***baba***aaa*b***")