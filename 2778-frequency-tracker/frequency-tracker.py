class FrequencyTracker:

    def __init__(self):
        
        self.hashmap = defaultdict(int)
        self.frequency = defaultdict(int)

    def add(self, number: int) -> None:
        
        old_frequency = self.hashmap[number]

        if old_frequency > 0:

            self.frequency[old_frequency] -= 1
        
        self.hashmap[number] += 1

        new_frequency = self.hashmap[number]

        self.frequency[new_frequency] += 1


    def deleteOne(self, number: int) -> None:

        old_frequency = self.hashmap[number]

        if old_frequency > 0:

            self.frequency[old_frequency] -= 1

            self.hashmap[number] -= 1

            new_frequency = self.hashmap[number]

            self.frequency[new_frequency] += 1
        
    def hasFrequency(self, frequency: int) -> bool:
        
        return True if self.frequency[frequency] > 0 else False

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)