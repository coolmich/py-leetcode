from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        cc = Counter(magazine)
        for i in ransomNote:
            cc[i] -= 1
            if cc[i] < 0: return False
        return True