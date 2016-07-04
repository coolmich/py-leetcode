class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        mapi = {0:0, 1:8, 2:4, 3:12, 4:2, 5:10, 6:6, 7:14, 8:1, 9:9, 10:5, 11:13, 12:3, 13:11, 14:7, 15:15}
        i, num = 7, 0
        while i >= 0:
            num, i, n = num | mapi[n%16] << (i*4), i - 1, n/16
        return num