class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        hashmap = defaultdict(int)

        n = len(edges)
        
        for node1,node2 in edges:
            hashmap[node1] += 1
            hashmap[node2] += 1
        
        for value in hashmap:
            if hashmap[value] == n:
                return value