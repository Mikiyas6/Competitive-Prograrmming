class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        hash1 = Counter(arr1)
        hash2 = Counter(arr2)

        leftAlones = [value for value in arr1 if value not in hash2]
        leftAlones.sort()
        arr1.sort()

        results = []
        for value in arr2:
            results.extend([value]*hash1[value])
        results.extend(leftAlones)

        return results
