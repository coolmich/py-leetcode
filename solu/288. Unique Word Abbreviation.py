from collections import defaultdict
class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.mapi = defaultdict(set)
        for word in dictionary:
            self.mapi[self.transform(word)].add(word)

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        t = self.transform(word)
        if t not in self.mapi: return True
        if len(self.mapi[t]) == 1 and word in self.mapi[t]: return True
        return False

    def transform(self, word):
        if not len(word): return '0'
        return word[0] + str(len(word)) + word[-1]

# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")