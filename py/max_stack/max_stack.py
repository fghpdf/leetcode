import heapq
class MaxStack:

    def __init__(self):
        self.stack = []
        self.hp = []
        self.hpd = set() # remove element from heap
        self.sd = set() # remove element from sd
        self.id = 0

    def push(self, x: int) -> None:
        self.stack.append((self.id, x))
        heapq.heappush(self.hp, (-x, -self.id))
        self.id += 1

    def pop(self) -> int:
        x = self.top()
        self.hpd.add(self.stack[-1][0])
        self.stack.pop()
        return x

    def top(self) -> int:
        while self.stack[-1][0] in self.sd:
            self.sd.remove(self.stack[-1][0])
            self.stack.pop()
        return self.stack[-1][1]

    def peekMax(self) -> int:
        while -self.hp[0][1] in self.hpd:
            self.hpd.remove(-self.hp[0][1])
            heapq.heappop(self.hp)
        return -self.hp[0][0]

    def popMax(self) -> int:
        x = self.peekMax()
        _, nid = heapq.heappop(self.hp)
        self.sd.add(-nid)
        return x