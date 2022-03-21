from typing import Deque


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
          return None

        q, clones = Deque([node]), {node.val: Node(node.val, [])}
        while q:
          cur = q.popleft()
          curClone = clones[cur.val]

          for ngbr in cur.neighbors:
            if ngbr.val not in clones:
              clones[ngbr.val] = Node(ngbr.val, [])
              q.append(ngbr)

            curClone.neighbors.append(clones[ngbr.val])

        return clones[node.val]