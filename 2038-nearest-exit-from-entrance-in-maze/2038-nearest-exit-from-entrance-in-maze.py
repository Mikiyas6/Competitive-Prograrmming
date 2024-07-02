class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        

        from collections import deque

        rows, cols = len(maze), len(maze[0])
        visited = [[False] * cols for _ in range(rows)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] 

        queue = deque()
        queue.append((entrance[0], entrance[1]))
        visited[entrance[0]][entrance[1]] = True

        distance = 0
        while queue:
            levelSize = len(queue)

            for _ in range(levelSize):
                currentRow, currentCol = queue.popleft()

                if (currentRow != entrance[0] or currentCol != entrance[1]) and maze[currentRow][currentCol] == '.':
                    if currentRow == 0 or currentCol == 0 or currentRow == rows - 1 or currentCol == cols - 1:
                        return distance

                for dx, dy in directions:  
                    nextRow, nextCol = currentRow + dx, currentCol + dy

                    if nextRow >= 0 and nextRow < rows and nextCol >= 0 and nextCol < cols and not visited[nextRow][nextCol] and maze[nextRow][nextCol] != '+':
                        visited[nextRow][nextCol] = True
                        queue.append((nextRow, nextCol))

            distance += 1

        return -1
