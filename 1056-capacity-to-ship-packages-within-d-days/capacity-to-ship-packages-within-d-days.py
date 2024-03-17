class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def can_ship(weights, capacity, days):
            count_days = 1
            total_weight = 0
            for weight in weights:
                if total_weight + weight > capacity:
                    count_days += 1
                    total_weight = weight
                else:
                    total_weight += weight
            return count_days <= days

        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if can_ship(weights, mid, days):
                right = mid
            else:
                left = mid + 1
        return left