class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_max, right_max, water = [], None, 0
        for i in range(1, len(height)-1):
            left_max.append(max(0 if not len(left_max) else left_max[-1], height[i - 1]))
        for i in range(len(height)-2, 0, -1):
            right_max = max(right_max if right_max is not None else 0, height[i+1])
            l_max = left_max.pop()
            water += max(0, (min(l_max, right_max) - height[i]))
        return water