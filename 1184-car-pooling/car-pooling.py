class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        last_stop = 0

        for numPassengers, start, end in trips:

            last_stop = max(last_stop,end)
        
        prefix_sum = [0] * (last_stop+1)

        for numPassengers, start, end in trips:

            prefix_sum[start] += numPassengers
            prefix_sum[end] -= numPassengers
        
        cumulative = 0
        
        for index,value in enumerate(prefix_sum):

            cumulative += value

            if cumulative > capacity:

                return False
            
            prefix_sum[index] = cumulative
        
        return True

            


