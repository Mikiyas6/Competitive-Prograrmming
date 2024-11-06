class Solution:
    def lastRemaining(self, n: int) -> int:
        left_to_right = True
        interval = 1 # step in the algorithm
        last_remaining = n # last number in array
        
        # length of the array is > 1
        while n > 1:
            # if array length is odd or going right to left
            if n%2 == 1 or not left_to_right:
                last_remaining = last_remaining - interval # subtract interval
            
            n = int(n/2) # get new size of array
            left_to_right = not left_to_right
            interval *= 2 # get new interval
        
        return last_remaining