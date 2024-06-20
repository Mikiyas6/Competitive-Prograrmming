class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        def canPlaceBalls(min_force):
            # Place the first ball in the first basket
            count = 1
            last_position = position[0]
            
            for i in range(1, len(position)):
                if position[i] - last_position >= min_force:
                    count += 1
                    last_position = position[i]
                if count == m:
                    return True
            return False
        
        # Sort the positions to apply binary search on minimum distance
        position.sort()
        
        # Initialize binary search range
        left, right = 1, position[-1] - position[0]
        best = 0
        
        while left <= right:
            mid = (left + right) // 2
            if canPlaceBalls(mid):
                best = mid  # Update the best found result
                left = mid + 1  # Try for a larger minimum distance
            else:
                right = mid - 1  # Try for a smaller minimum distance
        
        return best