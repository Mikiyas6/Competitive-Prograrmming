class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        n = len(arr)
        new_list = []
        
        for i in range(len(arr)):
            

            # Finding the index of the maximum value
            max_value = max(arr[:n-i])
            index = arr.index(max_value)

            # Since it's that index we want, we append it to our list
            new_list.append(index+1)

            # Flip the list from the start upto the maximum element (Inclusive)
            lists = arr[:index+1]
            lists = lists[::-1]
            arr = lists + arr[index+1:]

            # Now since the max element is at the starting position, we will flip it to the next last position
            arr = arr[:n-i][::-1] 

            #Since we've done another flip, we insert it to our list
            new_list.append(n-i)
        
        return new_list


# class Solution:
#     def pancakeSort(self, arr: List[int]) -> List[int]:

#         def flip(index):

#             start = 0
#             end = index

#             while start < end:

#                 arr[start], arr[end] = arr[end], arr[start]

#                 start += 1
#                 end -= 1

#         n = len(arr)
#         output = []
        
#         for i in range(n-1,-1,-1):

#             max_index = i

#             for j in range(i-1,-1,-1):

#                 if arr[j] > arr[max_index]:

#                     max_index = j

#             if max_index != i:

#                 flip(max_index)
#                 flip(i)
#                 output.append(max_index+1)
#                 output.append(i+1)

#         return output




