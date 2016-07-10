class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack1.append(x)


    def pop(self):
        """
        :rtype: nothing
        """
        self.refill()
        self.stack2.pop()

    def peek(self):
        """
        :rtype: int
        """
        self.refill()
        return self.stack2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not len(self.stack1) and not len(self.stack2)

    def refill(self):
        if not len(self.stack2):
            while len(self.stack1):
                self.stack2.append(self.stack1.pop())