from collections import defaultdict
class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        def helper(depth, nestList, mapi):
            for item in nestList:
                if item.isInteger(): mapi[depth].append(item.getInteger())
                else: helper(depth+1, item.getList(), mapi)
        if not nestedList or not nestedList[0]: return 0
        mapi = defaultdict(list)
        helper(1, nestedList, mapi)
        if not mapi: return 0
        maxi, sumi = max(mapi.keys()), 0
        for i in range(1, maxi+2):
            sumi += sum(mapi[i])*(maxi-i+1)
        return sumi