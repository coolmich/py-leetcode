class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        stack = triangle[0]
        for i in range(1, len(triangle)):
            to_add = triangle[i]
            stack = [to_add[i] + min(stack[i-1] if 0<=i-1<len(stack) else 9999999,
                                    stack[i] if 0<=i<len(stack) else 9999999) for i in range(len(to_add))]
        return min(stack)


