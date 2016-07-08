class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        def helper(cor_list):
            cors = sorted(cor_list, key=lambda x:x[0])
            if cors[0][1] == cors[1][1]:
                return 0
            else:
                return cors[2][0] - cors[1][0]
        w = helper([(A, 0), (C, 0), (E, 1), (G, 1)])
        h = helper([(B, 0), (D, 0), (F, 1), (H, 1)])
        return (C-A)*(D-B) + (G-E)*(H-F) - w*h