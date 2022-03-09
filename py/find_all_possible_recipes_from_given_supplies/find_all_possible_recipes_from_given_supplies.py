from typing import List
import unittest

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        if len(recipes) == 0 or len(ingredients) == 0 or len(supplies) == 0:
          return []

        graph = {}
        for recipe in recipes:
          graph[recipe] = []
        
        canMake = {}
        supplies = set(supplies)

        def dfs(recipe:str) -> bool:
          if recipe not in canMake:
            canMake[recipe] = False
            canMake[recipe] = all([dfs(ingr) for ingr in graph[recipe]])
          return canMake[recipe]

        for i, recipe in enumerate(recipes):
          for ingr in ingredients[i]:
            if ingr not in supplies:
              graph[recipe].append(ingr if ingr in graph else recipe)

        res = []
        for recipe in recipes:
          if dfs(recipe):
            res.append(recipe)

        return res

class TestSolution(unittest.TestCase):
    def testFindAllRecipes(self):
      sol = Solution()
      self.assertEqual(sol.findAllRecipes(recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]), ["bread"])
      self.assertEqual(sol.findAllRecipes(recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]),  ["bread","sandwich"])
      self.assertEqual(sol.findAllRecipes(recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]), ["bread","sandwich","burger"])

if __name__ == '__main__':
  unittest.main()