class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:

        prefix_sum = [0] * (n+1)

        for first,last,seats in bookings:

            prefix_sum[first-1] += seats
            prefix_sum[last] -= seats
        
        cumulative = 0

        for index, value in enumerate(prefix_sum):

            cumulative += value

            prefix_sum[index] = cumulative
        
        return prefix_sum[:n]
        