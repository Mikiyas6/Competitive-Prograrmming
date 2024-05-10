class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        n = len(heaters)
        houses.sort()
        heaters.sort()
        
        max_radius = 0
        
        for house in houses:
            closest_heater_idx = bisect.bisect_left(heaters, house)

            if closest_heater_idx == 0:
                radius = heaters[0] - house
            elif closest_heater_idx == n:
                radius = house - heaters[-1]
            else:
                radius = min(heaters[closest_heater_idx] - house, house - heaters[closest_heater_idx - 1])
            
            max_radius = max(max_radius, radius)
        
        return max_radius
