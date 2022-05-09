from decimal import *
from typing import Dict, List
import unittest

class Transaction:
  def __init__(self, fromUser: str, toUser: str, tranRatio: int) -> None:
    self.fromUser = fromUser
    self.toUser = toUser
    self.tranRatio = tranRatio # 12.21% -> 1221

class User:
  def __init__(self, name: str, balance: str) -> None:
      self.name = name
      self.balance = Decimal(balance)
      
class CalcBalanceProcess:
  def calcUsersBalance(self, users: List[User], trans: List[Transaction]) -> Dict[str, Decimal]:
      userBalanceMap = {}
      for user in users:
        userBalanceMap[user.name] = user.balance

      for tran in trans:
        if tran.toUser not in userBalanceMap or tran.fromUser not in userBalanceMap:
          continue
        delta = Decimal(userBalanceMap[tran.fromUser]) * Decimal(tran.tranRatio) / Decimal(10000)
        # + balance if to
        oldToBalance = Decimal(userBalanceMap[tran.toUser])
        userBalanceMap[tran.toUser] = oldToBalance + delta
        # - balance if from
        oldFromBalance = Decimal(userBalanceMap[tran.fromUser])
        userBalanceMap[tran.fromUser] = oldFromBalance - delta

      return userBalanceMap
        
class TestCalcBalanceProcess(unittest.TestCase):
  def testCalcUsersBalance(self):
      p = CalcBalanceProcess()
      self.assertDictEqual(p.calcUsersBalance([User("qxx", "10"), User("tom", "0.83")], [Transaction("qxx", "tom", 1000)]), {"qxx": Decimal(9), "tom": Decimal("1.83")})


if __name__ == '__main__':
    unittest.main()
