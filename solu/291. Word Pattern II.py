from collections import defaultdict, Counter
class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        def possible_len(pattern, str):
            cc = Counter(list(pattern))
            mapi = {}
            for k in cc:
                mapi[k] = (len(str) - (len(pattern) - cc[k])) / cc[k]+1
            return mapi
            
        def helper(pattern, pidx, str, stridx, mapi, max_cnt):
            if pidx == len(pattern) or stridx == len(str):
                if pidx == len(pattern) and stridx == len(str): return 1
                return 0
            if pattern[pidx] in mapi:
                end = stridx + len(mapi[pattern[pidx]])
                if end > len(str): return 0#-1
                if str[stridx:end] == mapi[pattern[pidx]]: return helper(pattern, pidx+1, str, end, mapi, max_cnt)
                return 0
            else:
                i = 1
                while i < max_cnt[pattern[pidx]]:
                    if str[stridx:stridx+i] not in mapi.values():
                        mapi[pattern[pidx]] = str[stridx:stridx+i]
                        ret = helper(pattern, pidx+1, str, stridx+i, mapi, max_cnt)
                        if ret == 1: return 1
                        else:
                            mapi.pop(pattern[pidx])
                            # return -1
                    i += 1
                return 0#-1
        mapi, max_cnt = {}, possible_len(pattern, str)
        return helper(pattern, 0, str, 0, mapi, max_cnt) == 1