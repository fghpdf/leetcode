class ProductOfNumbers:

    def __init__(self):
        self.p = [1]

    def add(self, num: int) -> None:
        if num == 0:
          self.p = [1]
        else:
          self.p.append(self.p[-1]*num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.p):
          return 0
        else:
          return self.p[-1] / self.p[-k-1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

if __name__ == '__main__':
    obj = ProductOfNumbers()
    obj.add(3)
    obj.add(0)
    obj.add(2)
    obj.add(5)
    obj.add(4)
    print(obj.getProduct(2))
    print(obj.getProduct(3))
    print(obj.getProduct(4))
    obj.add(8)
    print(obj.getProduct(2))
    
