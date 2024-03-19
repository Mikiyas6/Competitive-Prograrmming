class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        if len(arr) == 1:

            return 1
        
        sign = ""

        l = 0

        longest = 0

        for r in range(1,len(arr)):

            if arr[r-1] > arr[r]:

                current_sign = ">"
            
            elif arr[r-1] < arr[r]:

                current_sign = "<"
            
            else:

                current_sign = "="

            
            if current_sign == "=":

                    sign = ""

                    l = r
            
            if current_sign == sign:

                l = r - 1

            sign = current_sign
            
            longest = max(longest,r-l+1)
        
        return longest