class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.nums = []
        while iterator.hasNext():
          self.nums.append(iterator.next())
        self.index = 0

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.nums[self.index]

    def next(self):
        """
        :rtype: int
        """
        res = self.nums[self.index]
        self.index += 1
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.index >= len(self.nums):
          return False

        return True