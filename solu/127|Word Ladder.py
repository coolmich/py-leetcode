class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        stack, level = [beginWord], 1
        while len(stack):
            newS = []
            for word in stack:
                for i in range(len(word)):
                    for l in 'abcdefghijklmnopqrstuvwxyz':
                        n = word[:i] + l + word[i+1:]
                        if n in wordList:
                            if n == endWord: return level+1
                            wordList.remove(n)
                            newS.append(n)
            stack, level = newS, level+1
        return 0
        