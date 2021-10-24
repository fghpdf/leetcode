'''
Author: fghpdf
Date: 2021-10-24 10:31:38
LastEditTime: 2021-10-24 10:53:23
LastEditors: fghpdf
'''
import unittest

class Solution:
    def countValidWords(self, sentence: str) -> int:
        if len(sentence) == 0:
          return 0

        ss = sentence.split(' ')
        res = 0
        for s in ss:
          if self.isValid(s):
            res += 1
        
        return res

    def isValid(self, sentence: str) -> bool:
        n = len(sentence)
        if n == 0:
          return False

        hyphenCount = 0
        punctuationCount = 0
        for i in range(n):
          c = sentence[i]
          if c == '-':
            if i == 0 or i == n - 1:
              return False
            if hyphenCount != 0:
              return False
            if not sentence[i+1].isalpha() or not sentence[i-1].isalpha():
              return False
            hyphenCount += 1
          
          if c == '!' or c == '.' or c == ',':
            if i != n - 1:
              return False
            if punctuationCount != 0:
              return False
            punctuationCount += 1
          if c.isdigit():
            return False

        return True
          

class TestSolution(unittest.TestCase):
    def testCountValidWords(self):
        sol = Solution()
        self.assertEqual(sol.countValidWords(sentence= " 62   nvtk0wr4f  8 qt3r! w1ph 1l ,e0d 0n 2v 7c.  n06huu2n9 s9   ui4 nsr!d7olr  q-, vqdo!btpmtmui.bb83lf g .!v9-lg 2fyoykex uy5a 8v whvu8 .y sc5 -0n4 zo pfgju 5u 4 3x,3!wl  fv4   s  aig cf j1 a i  8m5o1  !u n!.1tz87d3 .9    n a3  .xb1p9f  b1i a j8s2 cugf l494cx1! hisceovf3 8d93 sg 4r.f1z9w   4- cb r97jo hln3s h2 o .  8dx08as7l!mcmc isa49afk i1 fk,s e !1 ln rt2vhu 4ks4zq c w  o- 6  5!.n8ten0 6mk 2k2y3e335,yj  h p3 5 -0  5g1c  tr49, ,qp9 -v p  7p4v110926wwr h x wklq u zo 16. !8  u63n0c l3 yckifu 1cgz t.i   lh w xa l,jt   hpi ng-gvtk8 9 j u9qfcd!2  kyu42v dmv.cst6i5fo rxhw4wvp2 1 okc8!  z aribcam0  cp-zp,!e x  agj-gb3 !om3934 k vnuo056h g7 t-6j! 8w8fncebuj-lq    inzqhw v39,  f e 9. 50 , ru3r  mbuab  6  wz dw79.av2xp . gbmy gc s6pi pra4fo9fwq k   j-ppy -3vpf   o k4hy3 -!..5s ,2 k5 j p38dtd   !i   b!fgj,nx qgif "), 49)
        self.assertEqual(sol.countValidWords(sentence = "cat and  dog"), 3)
        self.assertEqual(sol.countValidWords(sentence = "!this  1-s b8d!"), 0)
        self.assertEqual(sol.countValidWords(sentence = "alice and  bob are playing stone-game10"), 5)
        self.assertEqual(sol.countValidWords(sentence = "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."), 6)
        self.assertEqual(sol.countValidWords(sentence = "a-b-c"), 0)
        self.assertEqual(sol.countValidWords(sentence = "a-"), 0)

if __name__ == '__main__':
    unittest.main()