class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        return self.helper(candidates, target)

    def helper(self, candidates, target):
        res = []
        if len(candidates) and candidates[0] <= target:
            if candidates[0] == target:
                return [[candidates[0]]]
            # include the first one
            with_first = self.helper(candidates, target - candidates[0])
            if len(with_first):
                res = [arr + [candidates[0]] for arr in with_first]
            # exclude the first one
            without_first = self.helper(candidates[1:], target)
            if len(without_first):
                res += without_first
        return res
