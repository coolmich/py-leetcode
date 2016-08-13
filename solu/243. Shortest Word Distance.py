class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        idx1 = idx2 = None
        dist = 2**31
        for idx, word in enumerate(words):
            if word == word1:
                idx1 = idx
            elif word == word2:
                idx2 = idx
            else: continue
            if idx1 is not None and idx2 is not None: dist = min(dist, abs(idx1-idx2))
        return dist