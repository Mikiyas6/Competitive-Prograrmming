from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(node):
            neighbors_list = []
            for i in range(4):
                digit = int(node[i])
                for diff in [-1, 1]:
                    new_digit = (digit + diff) % 10
                    neighbor = node[:i] + str(new_digit) + node[i+1:]
                    neighbors_list.append(neighbor)
            return neighbors_list

        visited = set(deadends)
        if '0000' in visited:
            return -1
        
        queue = deque([('0000', 0)])
        visited.add('0000')

        while queue:
            current, steps = queue.popleft()
            if current == target:
                return steps
            
            for neighbor in neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))
        
        return -1
