class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        hashmap = Counter(arr1)
        hashmap2 = Counter(arr2)
        hashset = []
        
        for value in arr1:
            if value not in hashmap2:
                hashset.append(value)
        hashset.sort()

        result = []

        for value in arr2:
            result.extend([value]*hashmap[value])
        
        result.extend(hashset)
        
        return result
