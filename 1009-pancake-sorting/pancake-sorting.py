class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        n = len(arr)

        output = []

        if sorted(arr) != arr:

            for i in range(n):

                if arr[:n-i-1]:

                    max_value = max(arr[:n-i])

                    index_of_max_value = arr[:n-i].index(max_value)

                    output.append(index_of_max_value + 1)

                    output.append(n-i)

                    arr[:index_of_max_value+1] = arr[:index_of_max_value+1][::-1]

                    arr[:n-i] = arr[:n-i][::-1]
        
        return output


        