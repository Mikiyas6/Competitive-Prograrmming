class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        if not arr:
            return 0

        if len(arr) == 1:
            return 1

        l = 0

        prev_sign = ""

        max_length = 0

        for r in range(1,len(arr)):

            # Determine the current sign

            if arr[r-1] > arr[r]:

                sign = ">"
            
            elif arr[r-1] < arr[r]:

                sign = "<"
            
            else:

                sign = "="

            # Calculate the current length

            length = r - l + 1

            # Shrinking the window size. The shrinking of the window depends on the sign you determined

            if sign == "=": # If the sign is "=" then the window we want to start our window from the current value in the array

                length -= 1
                l = r

            elif prev_sign == sign: # If the sign is simply different than before, then we want to start the window from r-1 value
                
                length -= 1
                l = r - 1

            max_length = max(max_length,length)

            prev_sign = sign
            
        return max_length

        
        
