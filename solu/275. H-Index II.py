class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        start, end = 0, len(citations) - 1
        while start <= end:
            mid = (start+end)/2
            cnt = len(citations) - mid
            if citations[mid] >= cnt:
                end = mid - 1
            else:
                start = mid + 1
        return len(citations) - start 