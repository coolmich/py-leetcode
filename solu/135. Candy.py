class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        stack = [1]*len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                stack[i] = stack[i-1]+1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                stack[i] = max(stack[i], stack[i+1]+1)
        return sum(stack)