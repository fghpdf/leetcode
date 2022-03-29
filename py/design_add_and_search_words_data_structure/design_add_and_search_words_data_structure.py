class TrieNode:
  def __init__(self):
    self.children = {}
    self.endNode = 0

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        root = self.root

        for symbol in word:
          root = root.children.setdefault(symbol, TrieNode())
        root.endNode = 1

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, i):
          if i == len(word):
            return node.endNode

          if word[i] == ".":
            for child in node.children:
              if dfs(node.children[child], i+1):
                return True

          if word[i] in node.children:
            return dfs(node.children[word[i]], i+1)

          return False
        
        return dfs(self.root, 0)

wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad"))
print(wordDictionary.search("bad"))
print(wordDictionary.search(".ad"))
print(wordDictionary.search("b.."))