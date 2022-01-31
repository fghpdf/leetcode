'''
Author: fghpdf
Date: 2022-01-31 09:00:13
LastEditTime: 2022-01-31 09:16:45
LastEditors: fghpdf
'''
from bisect import bisect_left
from typing import List
import unittest

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        if len(products) == 0:
            return []

        products.sort()
        
        res, prefix, i = [], "", 0
        for c in searchWord:
          prefix += c
          i = bisect_left(products, prefix, i)
          suggests = [w for w in products[i:i+3] if w.startswith(prefix)]
          res.append(suggests)
        
        return res
        

class TestSolution(unittest.TestCase):
    def testSuggestedProducts(self):
        sol = Solution()
        self.assertEqual(sol.suggestedProducts(products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"), [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
])
        self.assertEqual(sol.suggestedProducts(products = ["havana"], searchWord = "havana"), [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]])
        self.assertEqual(sol.suggestedProducts( products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"), [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]])
      
if __name__ == '__main__':
    unittest.main()