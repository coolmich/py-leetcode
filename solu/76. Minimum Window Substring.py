from collections import deque, Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        cnt, q, mini, c = Counter(list(t)), deque([]), s+s, 0
        for l in s:
            q.append(l)
            if l in cnt:
                cnt[l] -= 1
                if cnt[l] >= 0: c += 1
                while q:
                    if q[0] not in cnt:
                        q.popleft()
                    elif q[0] in cnt and cnt[q[0]] < 0:
                        cnt[q.popleft()] += 1
                    else: break
                if c == len(t) and len(q) < len(mini):
                    mini = ''.join(q)
        return mini if len(mini) < len(s)*2 else ''
 