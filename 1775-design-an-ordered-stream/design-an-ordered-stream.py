class OrderedStream:

    def __init__(self, n: int):
        
        self.size = n
        self.array = [None] * n
        self.pointer = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        
        self.array[idKey-1] = value
        counter = 0

        for i in range(self.pointer,self.size):

            if self.array[i]:

                counter += 1
            
            else:

                answer =  self.array[self.pointer:i]
                self.pointer = i
                return answer
        
        return self.array[self.pointer:]
        
        





# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)