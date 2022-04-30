import collections
from typing import List
import unittest

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        if len(equations) == 0:
          return []

        graph = {}
        
        def build_graph(equations, values):
            def add_edge(f, t, value):
                if f in graph:
                    graph[f].append((t, value))
                else:
                    graph[f] = [(t, value)]
            
            for vertices, value in zip(equations, values):
                f, t = vertices
                add_edge(f, t, value)
                add_edge(t, f, 1/value)
        
        def find_path(query):
            b, e = query
            
            if b not in graph or e not in graph:
                return -1.0
                
            q = collections.deque([(b, 1.0)])
            visited = set()
            
            while q:
                front, cur_product = q.popleft()
                if front == e:
                    return cur_product
                visited.add(front)
                for neighbor, value in graph[front]:
                    if neighbor not in visited:
                        q.append((neighbor, cur_product*value))
            
            return -1.0
        
        build_graph(equations, values)
        return [find_path(q) for q in queries]

class TestSolution(unittest.TestCase):
    def testCalcEquation(self):
      sol = Solution()
      self.assertEqual(sol.calcEquation(equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]), [6.00000,0.50000,-1.00000,1.00000,-1.00000])
      self.assertEqual(sol.calcEquation(equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]), [3.75000,0.40000,5.00000,0.20000])
      self.assertEqual(sol.calcEquation(equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]), [0.50000,2.00000,-1.00000,-1.00000])

if __name__ == '__main__':
    unittest.main()