class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.mapi = {}


    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.mapi[number] = 1 if number not in self.mapi else self.mapi[number] + 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for k in self.mapi:
            if value - k == k:
                if self.mapi[k] > 1: return True
            elif value-k in self.mapi: return True
        return False


# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)