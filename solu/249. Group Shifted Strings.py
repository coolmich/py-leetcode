from collections import defaultdict
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        def encode(word):
            res = []
            for i in range(1, len(word)):
                diff = (ord(word[i]) - ord(word[i-1]) + 26)%26
                res.append(str(diff))
            return ','.join(res)
        mapi = defaultdict(list)
        for word in strings:
            mapi[encode(word)].append(word)
        return [mapi[k] for k in mapi]