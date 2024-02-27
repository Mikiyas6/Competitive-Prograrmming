class RLEIterator:

    def __init__(self, encoding: List[int]):
        
        self.encoding = encoding
        self.ptr = 0

    def next(self, n: int) -> int:
        
        while self.ptr < len(self.encoding):
            if n <= self.encoding[self.ptr]:
                self.encoding[self.ptr] -= n
                return self.encoding[self.ptr + 1]
            else:
                n -= self.encoding[self.ptr]
                self.ptr += 2
                
        return -1

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)