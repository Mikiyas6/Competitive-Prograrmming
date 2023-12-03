class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        n = len(arr)
        output = []

        for i in range(n):

            if arr[:n-i-1]:

                max_index = arr.index(max(arr[:n-i]))

                output.extend([max_index + 1, n - i])

                arr[:max_index + 1] = reversed(arr[:max_index + 1])
                
                arr[:n-i] = reversed(arr[:n-i])

        return output

