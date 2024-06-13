class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        result = []
        destinations = set()

        for u, v in edges:
            destinations.add(v)
        
        for i in range(n):
            if i not in destinations:
                result.append(i)
        
        return result
        
