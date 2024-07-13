class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = sorted(zip(positions, healths, directions), key=lambda x: x[0])
        
        stack = []
        
        for pos, health, direction in robots:
            if direction == 'R':
                stack.append((pos, health, direction))
            else:
                while stack and stack[-1][2] == 'R' and health > 0:
                    top_pos, top_health, top_direction = stack[-1]
                    if top_health > health:
                        stack[-1] = (top_pos, top_health - 1, top_direction)
                        health = 0
                    elif top_health < health:
                        health -= 1
                        stack.pop()
                    else:
                        stack.pop()
                        health = 0
                
                if health > 0:
                    stack.append((pos, health, direction))
        
        survivors = {pos: health for pos, health, direction in stack}
        return [survivors[pos] for pos in positions if pos in survivors]