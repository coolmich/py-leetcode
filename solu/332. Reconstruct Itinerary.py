from collections import defaultdict
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        def dfs(dict, src, res, tickets):
            if len(res) == tickets: return True
            if not len(dict[src]): return False
            sortedL = sorted(dict[src])
            for dst in sortedL:
                dict[src].remove(dst)
                res.append(dst)
                if dfs(dict, dst, res, tickets):
                    return True
                res.pop()
                dict[src].append(dst)
            return False

        dep, res, ticket_num = defaultdict(list), ['JFK'], len(tickets)+1
        for u, v in tickets:
            dep[u].append(v)
        dfs(dep, 'JFK', res, ticket_num)
        return res

