import unittest

class Solution:
    def simplifyPath(self, path: str) -> str:
        if len(path) == 0:
            return ""

        folderStack = []
        for folder in path.split("/"):
          if folder == "." or folder == "":
              continue
          if folder == "..":
              if len(folderStack) > 0:
                folderStack.pop(-1)
              continue
          folderStack.append(folder)
        res = "/".join(folderStack)
        return "/" + res

class TestSolution(unittest.TestCase):
    def testSimplifyPath(self):
        sol = Solution()
        self.assertEqual(sol.simplifyPath("/home/"), "/home")
        self.assertEqual(sol.simplifyPath( "/../"), "/")
        self.assertEqual(sol.simplifyPath("/home//foo/"), "/home/foo")
        self.assertEqual(sol.simplifyPath("/a/./b/../../c/"), "/c")

if __name__ == "__main__":
    unittest.main()