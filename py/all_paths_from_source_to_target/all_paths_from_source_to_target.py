'''
Author: fghpdf
Date: 2021-10-24 17:05:48
LastEditTime: 2021-10-24 17:07:18
LastEditors: fghpdf
'''
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #edges cases:
        if not graph:
            return []
        
        # build di-graph
        d = {}
        for i in range(len(graph)):
            d[i] = graph[i] # one-way link
        
        # apply DFS on DAG
        n = len(graph)
        stack = [(0, [0])] # - store noth the (node, and the path leading to it)
        res = []
        while stack:
            node, path = stack.pop()
            # check leaf
            if node == n - 1:
                res.append(path)
            # traverse rest
            for nei in d[node]:
                stack.append((nei, path+[nei]))
        return res