class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

           farthest_destination = 0

        for passengers, start, end in trips:

            farthest_destination = max(farthest_destination,end)
        
        prefix_sum = [0] * (farthest_destination+1)

        for passengers,start,end in trips:

            prefix_sum[start] += passengers
            prefix_sum[end] -= passengers
        
        cumulative = 0

        for value in prefix_sum:

            cumulative += value

            if cumulative > capacity:

                return False
            
        return True

        # modified = []

        # for passengers, start, end in trips:

        #     modified.append([start,1,passengers])
        #     modified.append([end,0,passengers])
        
        # modified.sort()

        # for location, flag, passengers in modified:

        #     if flag == 1:

        #         capacity -= passengers
            
        #     else:

        #         capacity += passengers
            
        #     if capacity < 0:

        #         return False
        
        # return True
