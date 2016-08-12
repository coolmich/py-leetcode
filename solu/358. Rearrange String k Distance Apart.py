from collections import Counter, deque
import heapq
class Solution(object):
    def rearrangeString(self, str, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        mapi = Counter(list(str))
        h = [(-mapi[key], key) for key in mapi]
        heapq.heapify(h)
        q, res = deque(), []
        while h:
            cnt, letter = heapq.heappop(h)
            if not cnt: break
            res.append(letter)
            q.append((cnt + 1, letter))
            if len(q) >= k:
                heapq.heappush(h, q.popleft())
        return ''.join(res) if len(res) == len(str) else ''

        