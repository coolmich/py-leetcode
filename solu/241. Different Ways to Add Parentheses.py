from collections import defaultdict
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        def compute(operator, i1, i2):
            if operator == '+': return i1+i2
            if operator == '-': return i1-i2
            if operator == '*': return i1*i2

        def helper(cache, input):
            if input in cache: return cache[input]
            res = []
            for i in range(len(input)):
                if input[i] in ('+', '-', '*'):
                    l, r = helper(cache, input[:i]), helper(cache, input[i+1:])
                    for ll in l:
                        for rr in r:
                            res.append(compute(input[i], ll, rr))
            if not res:
                res.append(int(input))
            cache[input] = res
            return res

        cache = defaultdict(list)
        helper(cache, input)
        return cache[input]

