class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        houses.sort()
        heaters.sort()
        
        max_radius = 0
        
        # For each house, find the closest heater and calculate the distance
        for house in houses:
            closest_heater_idx = bisect.bisect_left(heaters, house)
            
            # Check if the closest heater is at the beginning or end of the heaters list
            if closest_heater_idx == 0:
                radius = heaters[0] - house
            elif closest_heater_idx == len(heaters):
                radius = house - heaters[-1]
            else:
                radius = min(heaters[closest_heater_idx] - house, house - heaters[closest_heater_idx - 1])
            
            max_radius = max(max_radius, radius)
        
        return max_radius
