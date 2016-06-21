class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a, b, res, i, c = list(reversed(a)), list(reversed(b)), [], 0, 0
        while i < max(len(a), len(b)):
            new_bi = (int(a[i]) if i < len(a) else 0) + (int(b[i]) if i < len(b) else 0) + c
            res.append(str(new_bi%2))
            i += 1
            if new_bi >= 2:
                c = 1
            else:
                c = 0
        if c:
            res.append('1')
        return "".join(list(reversed(res)))