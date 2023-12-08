class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        max_size = 0 

        l = 0

        previous_sign = sign = ""

        if len(arr) == 1:

            return 1

        for r in range(1,len(arr)):

            if arr[r-1] > arr[r]:

                current_sign = ">"
            
            elif arr[r-1] < arr[r]:

                current_sign = "<"
            
            else:

                current_sign = "="

            if current_sign == previous_sign:

                l = r - 1
            
            else:

                if current_sign == "=":

                    l = r
                
                    previous_sign = ""
                
                else:

                    previous_sign = current_sign
            
            max_size = max(max_size, r-l+1)
    
        return max_size
            
                
