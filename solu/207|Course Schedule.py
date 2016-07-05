from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        in_degree, out = defaultdict(int), defaultdict(list)
        for u, v in prerequisites:
            in_degree[v] += 1
            out[u].append(v)
        source = [i for i in range(numCourses) if in_degree[i] == 0]
        while len(source):
            newS = []
            for s in source:
                for v in out[s]:
                    in_degree[v] -= 1
                    if not in_degree[v]:
                        newS.append(v)
            source = newS
        return sum(in_degree.values()) == 0