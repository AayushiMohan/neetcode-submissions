class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()

            current = current.children[char]

        current.isEnd = True

    def search(self, word):
        
        def dfs(index, node):
            if index == len(word):
                return node.isEnd

            char = word[index]

            if char != '.':
                if char not in node.children:
                    return False

                return dfs(index + 1, node.children[char])

            for child in node.children.values():
                if dfs(index + 1, child):
                    return True

            return False

        return dfs(0, self.root)