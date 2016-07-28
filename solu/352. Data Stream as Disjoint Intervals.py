# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # head would store all the valid interval head
        self.head = set([])
        # mapi used to store all the numbers, in specific in an interval head and tail would point each other
        self.mapi = {}

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        if val in self.mapi: return
        if val-1 not in self.mapi and val+1 not in self.mapi:
            self.mapi[val] = val
            self.head.add(val)
        elif val-1 in self.mapi and val+1 in self.mapi:
            newH, newT = self.mapi[val-1], self.mapi[val+1]
            self.mapi[val-1], self.mapi[val], self.mapi[val+1] = 0, 0, 0
            self.mapi[newH], self.mapi[newT] = newT, newH
            self.head.discard(val+1)
        elif val-1 in self.mapi:
            head = self.mapi[val-1]
            self.mapi[val-1] = 0
            self.mapi[val], self.mapi[head] = head, val
        else:
            tail = self.mapi[val+1]
            self.mapi[val+1] = 0
            self.mapi[val], self.mapi[tail] = tail, val
            self.head.discard(val+1)
            self.head.add(val)

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        heads = sorted([head for head in self.head])
        return [[head, self.mapi[head]] for head in heads]



# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()