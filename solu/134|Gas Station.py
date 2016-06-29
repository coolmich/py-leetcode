class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        curG, curI, start = 0, 0, 0
        while curI < len(gas):
            curG += (gas[curI] - cost[curI])
            if curG < 0:
                start, curG = curI+1, 0
            curI += 1
        if start == len(gas): return -1
        curI = 0
        while curI < start:
            curG += (gas[curI] - cost[curI])
            if curG < 0: return -1
            curI += 1
        return start