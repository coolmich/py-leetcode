from collections import defaultdict, deque
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def cmp(word1, word2):
            for i in range(min(len(word1), len(word2))):
                if word1[i] != word2[i]: return (word1[i], word2[i])
            return (None, None)
        alpha = set(list(''.join(words)))
        if len(alpha) == 1: return alpha.pop()
        in_deg, edg = defaultdict(int), defaultdict(list)
        for i in range(1, len(words)):
            u, v = cmp(words[i-1], words[i])
            in_deg[v] += 1
            edg[u].append(v)
        q, stack = deque(), []
        for k in edg:
            if not in_deg[k]: q.append(k)
        while q:
            u = q.popleft()
            stack.append(u)
            for v in edg[u]:
                in_deg[v] -= 1
                if not in_deg[v]: q.append(v)
            edg.pop(u)
        if len(edg): return ''
        for item in stack: alpha.remove(item)
        return ''.join(stack + list(alpha))