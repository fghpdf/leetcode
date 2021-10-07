'''
Author: fghpdf
Date: 2021-10-07 09:32:19
LastEditTime: 2021-10-07 09:41:30
LastEditors: fghpdf
'''


from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Helper:
  def listToListNode(self, numbers: List[int]) -> Optional[ListNode]:
    if len(numbers) == 0:
      return
    head = ListNode(numbers[0])
    move = head
    for index in range(len(numbers)):
      if index == 0:
        continue
      
      node = ListNode(numbers[index])
      move.next = node
      move = node

    return head

if __name__ == '__main__':
  helper = Helper()
  print(helper.listToListNode([1,2,3]))

