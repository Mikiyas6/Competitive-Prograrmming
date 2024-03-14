class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        n = len(arr)

        if n < 3:

            return False

        max_index = arr.index(max(arr))

        first_part = arr[:max_index+1]
        second_part = arr[max_index:]

        print(first_part)
        print(second_part)

        if len(first_part) < 2 or len(second_part) < 2:

            return False

        i = 0
        j = i + 1

        while j < len(first_part):

            if first_part[j] <= first_part[i]:

                return False
            
            i += 1
            j += 1
        
        i = 0
        j = i + 1

        while j < len(second_part):

            if second_part[j] >= second_part[i]:

                return False

            i += 1
            j += 1
        
        return True

        # i = 1
        # j = n - 2

        # while i <= j:

        #     if arr[i] <= arr[i-1] or arr[j] <= arr[j+1]:

        #         return False
            
        #     i += 1
        #     j -= 1
        
        # return True