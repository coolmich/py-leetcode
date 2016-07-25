class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        mod = 1
        for c in b:
            mod = ((mod**10)%1337 * a**c) % 1337
        return mod