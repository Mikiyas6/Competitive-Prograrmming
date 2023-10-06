class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        n = len(arr)
        new_list = []
        
        for i in range(len(arr)):

            if arr[:n-i-1]:
                
                max_value = max(arr[:n-i])
                index = arr.index(max_value)
               
                new_list.append(index+1)


                lists = arr[:index+1]
                lists = lists[::-1]

                arr = lists + arr[index+1:]

                arr = arr[:n-i][::-1] + arr[n-i:]

                new_list.append(n-i)
        
        return new_list
