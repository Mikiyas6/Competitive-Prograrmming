class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        n = len(arr)
        maxValue = n
        result = []
        if sorted(arr) != arr:
            for i in range(n-1):
                # Find the index of the maximum value with in the specified range
                index = arr[:n-i].index(maxValue)
                # Store that index along with the 1 index in result
                result.extend([index+1,n-i])
                # Flip the array twice
                arr[:index+1] = arr[:index+1][::-1]
                arr[:n-i] = arr[:n-i][::-1]
                # Look for the next max Value
                maxValue -= 1
            result.append(1)
        return result



        