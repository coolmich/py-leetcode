from collections import OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.c = capacity
        self.mapi = OrderedDict()

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.mapi:
            ret = self.mapi.pop(key)
            self.mapi[key] = ret
            return ret
        return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.mapi:
            self.mapi.pop(key)
        self.mapi[key] = value
        if len(self.mapi) > self.c:
            self.mapi.popitem(last=False)