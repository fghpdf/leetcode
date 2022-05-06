from typing import List
from collections import defaultdict
class Node:
    def __init__(self):
        self.child=defaultdict(Node)
        self.content=""

class FileSystem:

    def __init__(self):
        self.root = Node()

    def find(self, path: str) -> Node:
        curr = self.root
        if len(path) == 1:
          return curr
        for word in path.split("/")[1:]:
          curr = curr.child[word]
        return curr
        
    def ls(self, path: str) -> List[str]:
        curr = self.find(path)
        if curr.content:
          #  file path, returns a list that only contains this file's name.
          return [path.split("/")[-1]]
        return sorted(curr.child.keys())

    def mkdir(self, path: str) -> None:
        self.find(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self.find(filePath)
        curr.content += content

    def readContentFromFile(self, filePath: str) -> str:
        curr = self.find(filePath)
        return curr.content