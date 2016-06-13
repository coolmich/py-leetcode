class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common_str = ""
        if len(strs) == 0: return common_str
        for idx, s in enumerate(strs[0]):
            for str in strs[1:]:
                if idx >= len(str) or str[idx] != s:
                    return common_str
            common_str += s
        return common_str