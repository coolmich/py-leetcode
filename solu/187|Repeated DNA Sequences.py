class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        num, res, mapi = 0, set([]), {}
        dic = {'A': 0, 'C': 1, 'T': 2, 'G': 3}
        for i in range(len(s)):
            num = ((num << 2) | dic[s[i]]) & 0xFFFFF
            if i >= 9:
                if num not in mapi: mapi[num] = 1
                else: mapi[num] = mapi[num] + 1
                if mapi[num] == 2: res.add(s[i-9:i+1])
        return list(res)
