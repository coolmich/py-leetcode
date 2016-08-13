class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        ups, stack = [0]*length, [0]
        for s,e,i in updates:
            ups[s] += i
            if e < len(ups) -1: ups[e+1] -= i
        for u in ups:
            stack.append(stack[-1]+u)
        return stack[1:]
        