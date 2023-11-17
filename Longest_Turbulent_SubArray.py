class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        previous_sign = ""
        l = 0
        max_length = 0

        if len(arr) == 1:

            return 1

        for r in range(1,len(arr)):

            if arr[r-1] > arr[r]:

                sign = ">"

            elif arr[r-1] < arr[r]:

                sign = "<"

            else:

                sign = "="

            if sign == previous_sign:

                l = r - 1

            if sign == "=":

                l = r

            max_length = max(max_length,r-l+1)
            previous_sign = sign

        return max_length
