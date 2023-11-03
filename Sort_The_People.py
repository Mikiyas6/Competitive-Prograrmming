class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        n = len(names)

        for i in range(len(names)):
            swapped = False

            for j in range(0, n-i-1):
                if heights[j+1] > heights[j]:
                    heights[j], heights[j+1] = heights[j+1], heights[j]
                    names[j], names[j+1] = names[j+1], names[j]
                    swapped = True

            if not swapped:
                break
        
        return names


        ### Bubble Sort #####
        #####################

        # n = len(heights)

        # for i in range(n):

        #     swapped = False

        #     for j in range(n-i-1):

        #         if heights[j+1] > heights[j]:

        #             heights[j], heights[j+1] = heights[j+1], heights[j]
        #             names[j], names[j+1] = names[j+1], names[j]
        #             swapped = True
            
        #     if not swapped:
        #         break

        # return names


        #### Selection Sort #####
        #########################

        # n = len(heights)

        # for i in range(n):

        #     max_index = i

        #     for j in range(i+1,n):

        #         if max(heights[max_index],heights[j]) != heights[max_index]:

        #             max_index = j
            
        #     heights[i], heights[max_index], = heights[max_index], heights[i]
        #     names[i], names[max_index] = names[max_index], names[i]
        
        # return names


        # n = len(names)

        # for i in range(1,n):

        #     key = heights[i]
        #     key_value = names[i]
        #     j = i - 1

        #     while j >= 0 and key > heights[j]:

        #         heights[j+1] = heights[j]
        #         names[j+1] = names[j]
        #         j -= 1
            
        #     heights[j+1] = key
        #     names[j+1] = key_value

        # return names


        ### Counting Sort ####
        ######################


        # dictionary = {}

        # n = len(heights)

        # for i in range(n):

        #     dictionary[heights[i]] = names[i]

        # max_value = max(heights)

        # frequency = [0] * (max_value+1)

        # for value in heights:

        #     frequency[value] += 1

        # sorted_array = []

        # for i in range(len(frequency)):

        #     if frequency[i]:

        #         length = len(sorted_array)
        #         value = frequency[i]

        #         sorted_array[length:length+value] = [i] * value

        # sorted_array = sorted_array[::-1]

        # new_names = [dictionary[value] for value in sorted_array]

        # return new_names

      
      



        




        

