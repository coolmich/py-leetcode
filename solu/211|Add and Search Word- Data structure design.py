class TrieNode(object):
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for l in word:
            idx = ord(l) - ord('a')
            if cur.children[idx] is None:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.end = True


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def helper(node, word):
            if not len(word): return node.end
            cur, l = node, word[0]
            if l == '.':
                for i in range(26):
                    if cur.children[i] is not None and helper(cur.children[i], word[1:]):
                        return True
                return False
            else:
                idx = ord(l) - ord('a')
                return cur.children[idx] is not None and helper(cur.children[idx], word[1:])
        return helper(self.root, word)



# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")