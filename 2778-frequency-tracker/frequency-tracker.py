# class FrequencyTracker:

#     def __init__(self):
        
#         self.hashmap = defaultdict(int)
#         self.frequency = defaultdict(list)

#     def add(self, number: int) -> None:

#         ######## For the frequency Hashmap ########

#             frequency = self.hashmap[number]

#             if frequency != 0:

#                 list_of_numbers = self.frequency[frequency]

#                 if number in list_of_numbers:

#                     list_of_numbers.remove(number)

#                 self.frequency[frequency] = list_of_numbers

#                 if not self.frequency[frequency]:

#                     del self.frequency[frequency]

#             self.frequency[frequency+1].append(number)

#             ####### For the main hashmap ###########
            
#             self.hashmap[number] += 1

#     def deleteOne(self, number: int) -> None:

#         if str(number).isdigit() and number in self.hashmap:

#             ######## For the frequency Hashmap ########

#             frequency = self.hashmap[number]

#             if frequency != 0:

#                 list_of_numbers = self.frequency[frequency]

#                 if number in list_of_numbers:

#                     list_of_numbers.remove(number)

#                 self.frequency[frequency] = list_of_numbers

#             if not self.frequency[frequency]:

#                 del self.frequency[frequency]

#             if frequency - 1 != 0:

#                 self.frequency[frequency-1].append(number)

#             ####### For the main hashmap ###########
            
#             self.hashmap[number] -= 1
            
#             if not self.hashmap[number]:

#                 del self.hashmap[number]

#     def hasFrequency(self, frequency: int) -> bool:

#         if frequency in self.frequency:
        
#            return True
class FrequencyTracker:

    def __init__(self):
        self.vals = defaultdict(int)
        self.freq = defaultdict(int)
        

    def add(self, number: int) -> None:
        old_freq = self.vals[number]

        if old_freq > 0:
            self.freq[old_freq] -= 1
        
        self.vals[number] += 1

        new_freq = self.vals[number]
        self.freq[new_freq] += 1
        
        

    def deleteOne(self, number: int) -> None:
        old_freq = self.vals[number]

        if old_freq > 0:
            self.freq[old_freq] -= 1
            self.vals[number] -= 1

            new_freq = self.vals[number]
            self.freq[new_freq] += 1
        

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)

# # Your FrequencyTracker object will be instantiated and called as such:
# # obj = FrequencyTracker()
# # obj.add(number)
# # obj.deleteOne(number)
# # param_3 = obj.hasFrequency(frequency)