from collections import deque

class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)]) 
        visited = set([(0, 1)])    
        
        while queue:
            pos, speed, steps = queue.popleft()
            
            if pos == target:
                return steps
            
            # Accelerate (A)
            new_pos, new_speed = pos + speed, speed * 2
            if (new_pos, new_speed) not in visited and 0 < new_pos < 2 * target:
                queue.append((new_pos, new_speed, steps + 1))
                visited.add((new_pos, new_speed))
            
            # Reverse (R)
            new_speed = -1 if speed > 0 else 1
            if (pos, new_speed) not in visited:
                queue.append((pos, new_speed, steps + 1))
                visited.add((pos, new_speed))
        
        return -1

