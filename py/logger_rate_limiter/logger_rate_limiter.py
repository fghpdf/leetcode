'''
Author: fghpdf
Date: 2022-02-07 03:18:44
LastEditTime: 2022-02-07 03:22:36
LastEditors: fghpdf
'''
class Logger:

    def __init__(self):
      self.messageNextValidDict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
      nextValidTime = self.messageNextValidDict.get(message, 0)
      if nextValidTime <= timestamp:
          self.messageNextValidDict[message] = timestamp + 10
          return True
      
      return False
      
