class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        def plus_one(arr):
            return [i+1 for i in arr]
        base = [0, 1, 1, 2]
        while num >= len(base):
            base += plus_one(base)
        return base[:num+1]