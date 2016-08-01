class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        def helper(s1, s2, cache):
            if (s1,s2) in cache: return cache[(s1,s2)]
            if s1 == s2:
                cache[(s1,s2)] = True
                return True
            if len(s1) != len(s2) or sorted(s1) != sorted(s2):
                cache[(s1,s2)] = False
                return False
            for i in range(1,len(s1)):
                if helper(s1[:i], s2[:i], cache) and helper(s1[i:], s2[i:], cache):
                    cache[(s1,s2)] = True
                    return True
                if helper(s1[:i], s2[-i:], cache) and helper(s1[i:], s2[:-i], cache):
                    cache[(s1,s2)] = True
                    return True
            cache[(s1,s2)] = False
            return False
        cache = {}
        return helper(s1, s2, cache)

        # if len(s1) != len(s2): return False
        # dp = [[[0 for i in range(len(s1))] for j in range(len(s1))] for k in range(len(s1)+1)]
        # for i in range(len(s1)):
        #     for j in range(len(s1)):
        #         dp[1][i][j] = 1 if s1[i] == s2[j] else 0
        # for gp in range(2, len(s1)+1):
        #     for start1 in range(len(s1)-gp+1):
        #         for start2 in range(len(s1)-gp+1):
        #             end1, end2 = start1+gp-1, start2+gp-1
        #             for i in range(1,gp):
        #                 if (dp[i][start1][start2] and dp[gp-i][start1+i][start2+i]) or (dp[i][start1][end2-i+1] and dp[gp-i][start1+i][start2]):
        #                     dp[gp][start1][start2] = 1
        #                     break
        # return dp[len(s1)][0][0] == 1