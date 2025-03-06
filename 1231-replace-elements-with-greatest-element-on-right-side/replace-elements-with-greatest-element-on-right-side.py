class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_value = -1
        result = []
        for i in range(len(arr)-1,-1,-1):
            result.append(max_value)
            max_value = max(max_value,arr[i])
        return result[::-1]