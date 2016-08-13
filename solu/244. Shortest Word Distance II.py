from collections import defaultdict
class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.mapi = defaultdict(list)
        for idx, word in enumerate(words):
            self.mapi[word].append(idx)

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dist, li1, li2, i1, i2 = 2**31, self.mapi[word1], self.mapi[word2], 0, 0
        while i1 < len(li1) and i2 < len(li2):
            dist = min(dist, abs(li1[i1] - li2[i2]))
            if li1[i1] > li2[i2]: i2 += 1
            else: i1 += 1
        return dist


# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")