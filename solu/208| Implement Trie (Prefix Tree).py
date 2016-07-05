class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = [None] * 26
        self.end = 0


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for l in word:
            if cur.children[ord(l) - 97] is None:
                cur.children[ord(l) - 97] = TrieNode()
            cur = cur.children[ord(l) - 97]
        cur.end = 1



    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for l in word:
            cur = cur.children[ord(l) - 97]
            if cur is None: return False
        return cur.end == 1



    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for l in prefix:
            cur = cur.children[ord(l) - 97]
            if cur is None: return False
        return True

# trie = Trie()
# trie.insert("a")
# trie.search("a")