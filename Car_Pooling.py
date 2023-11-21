class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        modified = []

        for passengers, start, end in trips:

            modified.append([start,1,passengers])
            modified.append([end,0,passengers])
        
        modified.sort()

        for location, flag, passengers in modified:

            if flag == 1:

                capacity -= passengers
            
            else:

                capacity += passengers
            
            if capacity < 0:

                return False
        
        return True
