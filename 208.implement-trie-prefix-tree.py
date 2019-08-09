#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
# solution #1
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Trie = dict()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.Trie
        for i in word:
            if i not in cur:
                cur[i] = dict()

            cur = cur[i]
        cur[0] = None

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.Trie
        for i in word:
            if i not in cur:
                return False
            cur = cur[i]
        if 0 in cur:
            return True
                

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.Trie
        for i in prefix:
            if i not in cur:
                return False
            cur = cur[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# solution #2
'''
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = []

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        self.root.append(word)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if word in self.root:
            return True
        else:
            return False


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if not self.root:
            return False
        for i in range(len(self.root)):
            if prefix == self.root[i][:len(prefix)]:
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
'''
