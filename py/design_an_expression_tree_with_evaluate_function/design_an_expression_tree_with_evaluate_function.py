'''
Author: fghpdf
Date: 2022-02-05 10:10:49
LastEditTime: 2022-02-05 10:19:30
LastEditors: fghpdf
'''
import abc 
from abc import ABC, abstractmethod
from typing import List 

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass

class BinaryNode(Node):
    def __init__(self, _left, _right):
        self.left = _left
        self.right = _right
    def evaluate(self) -> int:
        pass

class Plus(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate()+self.right.evaluate()

class Minus(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate()-self.right.evaluate()

class Mul(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate()*self.right.evaluate()

class Div(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate()//self.right.evaluate()

class Num(Node):
    def __init__(self, _value):
        self.value = _value
    def evaluate(self) -> int:
        return self.value


class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
      operators = {'+':Plus, '-':Minus, '*':Mul, '/':Div}
      stk = []
      for token in postfix:
        if token in operators:
          right = stk.pop()
          left = stk.pop()
          stk.append(operators[token](left, right))
        else:
          stk.append(Num(int(token)))
      return stk[0]

        