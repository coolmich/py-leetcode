class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def encode(word):
            res = 0
            for l in word:
                res |= (1<<(ord(l) - 97))
            return res

        mapi, maxi = {word:encode(word) for word in words}, 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not (mapi[words[i]] & mapi[words[j]]):
                    maxi = max(maxi, len(words[i])*len(words[j]))
        return maxi