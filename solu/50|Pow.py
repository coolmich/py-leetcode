class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0: return 1
        neg, n = n < 0, abs(n)
        stack, tmp = [x], n>>1
        while tmp:
            stack.append(stack[-1]*stack[-1])
            tmp >>= 1
        res, tmp = stack[-1], n - (1<<(len(stack)-1))
        while tmp:
            tmp_ = 1
            while (1<<tmp_) <= tmp/2.0: tmp_ += 1
            res *= stack[tmp_ - 1]
            tmp -= (1<<tmp_-1)
        return res if not neg else 1.0/res
