class Solution:
    def findLucky(self, arr: List[int]) -> int:
        largest = -1
        hashmap = Counter(arr)
        for value in set(arr):
            if value == hashmap[value]:
                largest = max(largest,value)
        return largest