# Definition for a undirected graph node
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node: return node
        mapi, stack, i = {}, [node], 0
        while i < len(stack):
            nn = stack[i]
            if nn not in mapi: mapi[nn] = UndirectedGraphNode(nn.label)
            stack += [n for n in nn.neighbors if n not in mapi]
            i += 1
        for oldN, newN in mapi.items():
            newN.neighbors = [mapi[n] for n in oldN.neighbors]
        return mapi[node]