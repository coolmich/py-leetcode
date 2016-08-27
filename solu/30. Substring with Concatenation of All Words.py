from collections import deque, Counter
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words or not s: return []
        wl, ret = len(words[0]), []
        for i in range(wl):
            q, mapi = deque(), Counter(words)
            while i <= len(s) - wl:
                ww = s[i:i+wl]
                if ww not in mapi:
                    while q: mapi[q.popleft()] += 1
                else:
                    if not mapi[ww]:
                        while not mapi[ww]:
                            mapi[q.popleft()] += 1
                    q.append(ww)
                    mapi[ww] -= 1
                    if len(q) == len(words):
                        ret.append(i-wl*len(words)+wl)
                        mapi[q.popleft()] += 1
                i += wl
        return ret