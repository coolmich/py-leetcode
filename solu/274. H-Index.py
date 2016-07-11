class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = sorted(citations, reverse=True)
        for idx,item in enumerate(citations):
            if item < idx + 1:
                return idx
        return len(citations)