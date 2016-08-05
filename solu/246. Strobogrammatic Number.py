class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        mapi = {'1':'1', '6':'9', '8':'8', '9':'6', '0':'0'}
        l, r = 0, len(num)-1
        while l <= r:
            if num[l] not in mapi or mapi[num[l]] != num[r]: return False
            l, r = l+1, r-1
        return True
    