class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # Step 1: Calculate the degree of each city
        degree = [0] * n
        for road in roads:
            degree[road[0]] += 1
            degree[road[1]] += 1
        
        # Step 2: Sort cities by degree
        sorted_cities = sorted(range(n), key=lambda x: degree[x], reverse=True)
        
        # Step 3: Assign values optimally
        values = [0] * n
        for i in range(n):
            values[sorted_cities[i]] = n - i
        
        # Step 4: Compute the total importance
        total_importance = 0
        for road in roads:
            total_importance += values[road[0]] + values[road[1]]
        
        return total_importance