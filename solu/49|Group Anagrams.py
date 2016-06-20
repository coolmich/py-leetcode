from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mapi = defaultdict(list)
        for str in strs:
            mapi[''.join(sorted(str))].append(str)
        return [mapi[k] for k in mapi]