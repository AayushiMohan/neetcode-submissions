class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()

            current = current.children[char]

        current.isEnd = True

    def search(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                return False

            current = current.children[char]

        return current.isEnd

    def startsWith(self, prefix):
        current = self.root

        for char in prefix:
            if char not in current.children:
                return False

            current = current.children[char]

        return True    