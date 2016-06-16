class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        oldSeq, newSeq = '1', '1'
        while n > 1:
            newSeq, i = '', 0
            while i < len(oldSeq):
                cnt = 1
                while i < len(oldSeq)-cnt and oldSeq[i] == oldSeq[i+cnt]:
                    cnt += 1
                newSeq += str(cnt) + oldSeq[i]
                i += cnt
            oldSeq = newSeq
            n -= 1
        return oldSeq