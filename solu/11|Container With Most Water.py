class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lh_idx, rh_idx = 0, len(height)-1
        max_area = min(height[0], height[-1])*(len(height)-1)
        while lh_idx < rh_idx:
            if height[lh_idx] < height[rh_idx]:
                lh_idx += 1
            else:
                rh_idx -= 1
            max_area = max(max_area, min(height[lh_idx], height[rh_idx])*(rh_idx - lh_idx))
        return max_area