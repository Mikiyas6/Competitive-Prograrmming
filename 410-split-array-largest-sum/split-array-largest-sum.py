class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def can_ship(nums, capacity, ships):
            allowed_number_of_ships = ships
            ships_count = 1
            total_weight = 0
            for weight in nums:
                if total_weight + weight > capacity:
                    ships_count += 1
                    total_weight = weight
                else:
                    total_weight += weight
            
            if ships_count > allowed_number_of_ships:
                return False
            return True

        # Since each day there's only one ship transporting the packages,
        # We can consider the number of days, as the number of ships that are available to us
        ships = k
        left, right = max(nums), sum(nums)
        result = right

        while left <= right:
            capacity = left + (right - left) // 2
            if can_ship(nums, capacity, ships):
                result = min(result,capacity)
                right = capacity - 1
            else:
                left = capacity + 1
        return result