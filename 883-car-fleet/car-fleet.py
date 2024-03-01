class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        current_time = 0

        for pos, spd in cars:
            time_to_target = (target - pos) / spd
            if time_to_target > current_time:
                fleets += 1
                current_time = time_to_target

        return fleets