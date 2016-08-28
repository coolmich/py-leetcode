class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack, maxi, heights = [], 0, [0] + heights + [0]
        for idx, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                item = stack.pop()
                maxi = max(maxi, (idx-stack[-1]-1)*heights[item])
            stack.append(idx)
        return maxi