class NumberContainers:

    def __init__(self):
        self.hashmap = defaultdict(list)
        self.tracer = defaultdict(int)
        
    def change(self, index: int, number: int) -> None:
        heappush(self.hashmap[number],index)
        if self.tracer[index]:
            if self.tracer[index] != number:
                heapp = self.hashmap[self.tracer[index]]
                heapp[:] = [x for x in heapp if x != index]  
                heapify(heapp)
                self.hashmap[self.tracer[index]] = heapp
        self.tracer[index] = number

    def find(self, number: int) -> int:
        return self.hashmap[number][0] if self.hashmap[number] else -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)