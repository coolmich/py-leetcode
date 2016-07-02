class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1, v2 = [int(i) for i in version1.split('.')], [int(j) for j in version2.split('.')]
        if len(v1) > len(v2): v2 += [0] * (len(v1) - len(v2))
        elif len(v1) < len(v2): v1 += [0] * (len(v2) - len(v1))
        for i in xrange(min(len(v1), len(v2))):
            if v1[i] > v2[i]: return 1
            elif v1[i] < v2[i]: return -1
        return 0
