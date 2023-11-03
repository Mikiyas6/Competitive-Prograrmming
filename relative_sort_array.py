class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        dictionary = {}

        for index,value in enumerate(arr2):

            dictionary[value] = index

        lists1 = []
        lists2 = []
        
        for value in arr1:

            if value not in arr2:
                lists1.append(value)
            else:
                lists2.append(value)

        def sorter(element):

            return dictionary[element]

        lists2.sort(key = sorter)
        lists1.sort()

        return lists2 + lists1

# class Solution:
#     def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
#         dictionary = {}

#         for i in range(len(arr2)):
#             dictionary[arr2[i]] = i

#         lists = []
        
#         def custom_comparator(items):

#             nonlocal lists
#             nonlocal dictionary
            
#             if items in dictionary.keys():
#                 return dictionary[items]
            
        
#         new_list1 = []
#         new_list2 = []

#         for value in arr1:
#             if value in arr2:
#                 new_list1.append(value)
#             else:
#                 new_list2.append(value)

#         new_list1.sort(key = custom_comparator)
#         new_list2.sort()

#         return new_list1 + new_list2
