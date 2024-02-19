class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        def dfs(counter):
            total = 0
            for char, count in counter.items():
                if count == 0:
                    continue
                total += 1  # Add the current character as a subsequence
                counter[char] -= 1
                total += dfs(counter)  # Recur with the reduced counter
                counter[char] += 1  # Backtrack
            return total

        tile_counts = Counter(tiles)
        return dfs(tile_counts)