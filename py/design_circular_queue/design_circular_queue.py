class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.max_size = k
        self.t = [0]*k
        self.front = self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.size  == self.max_size:
            return False
        
        if self.rear == -1:
            # one element in queue
            self.rear = self.front = 0
        else:
            self.rear = (self.rear+1)%self.max_size

        self.t[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
          return False
        
        if self.front == self.rear:
          self.front = self.rear = -1
        else:
          self.front = (self.front+1)%self.max_size
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size != 0:
          return self.t[self.front]

        return -1

    def Rear(self) -> int:
        if self.size != 0:
          return self.t[self.rear]
        return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size