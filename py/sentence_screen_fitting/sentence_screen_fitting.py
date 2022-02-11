'''
Author: fghpdf
Date: 2022-02-11 08:41:01
LastEditTime: 2022-02-11 08:45:32
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s = ' '.join(sentence)+' '
        start = 0
        for i in range(rows):
          start += cols - 1
          if s[start%len(s)] == ' ':
            start += 1
          elif s[(start+1)%len(s)] == ' ':
            start += 2
          else:
            while start > 0 and s[(start-1)%len(s)] != ' ':
              start -= 1
        return start / len(s)