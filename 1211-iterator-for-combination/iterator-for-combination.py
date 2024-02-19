class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        
        self.combinations = list(combinations(characters, combinationLength))
        self.index = 0

    def next(self) -> str:
        if self.hasNext():
            result = ''.join(self.combinations[self.index])
            self.index += 1
            return result

    def hasNext(self) -> bool:
        return self.index < len(self.combinations)
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()