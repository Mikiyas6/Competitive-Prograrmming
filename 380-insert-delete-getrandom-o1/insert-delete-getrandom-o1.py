class RandomizedSet:

    def __init__(self):
        self.set = set()

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        self.set.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.set:
            return False
        self.set.remove(val)
        return True

    def getRandom(self) -> int:
        return random.choice(list(self.set))
#     def __init__(self):
#         self.dict = defaultdict(int)
#         self.list = []

#     def insert(self, val: int) -> bool:
#         if val in self.dict:
#             return False
#         self.dict[val] = len(self.list)
#         self.list.append(val)
#         return True

#     def remove(self, val: int) -> bool:
#         if val not in self.dict:
#             return False
#         idx = self.dict[val]
#         last_val = self.list[-1]
#         self.list[idx] = last_val
#         self.dict[last_val] = idx
#         self.list.pop()
#         del self.dict[val]
#         return True

#     def getRandom(self) -> int:
#         return random.choice(self.list)

#     # def __init__(self):
#     #     self.set = []
#     #     self.index = 0
#     #     self.size = 0

#     # def insert(self, val: int) -> bool:
        
#     #     if val not in self.set:

#     #         self.set.append(val)

#     #         self.size += 1

#     #         return True
        
#     # def remove(self, val: int) -> bool:

#     #     if val in self.set:

#     #         self.set.remove(val)

#     #         self.size -= 1

#     #         return True
        
#     # def getRandom(self) -> int:

#     #     result = self.set[self.index % self.size]

#     #     self.index += 1

#     #     return result


# # Your RandomizedSet object will be instantiated and called as such:
# # obj = RandomizedSet()
# # param_1 = obj.insert(val)
# # param_2 = obj.remove(val)
# # param_3 = obj.getRandom()