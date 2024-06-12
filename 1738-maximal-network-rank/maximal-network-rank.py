class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        hashmap = defaultdict(list)

        for u, v in roads:

            hashmap[u].append(v)
            hashmap[v].append(u)
        
        maxNetwork = 0
        for i in range(n):
            rank1 = len(hashmap[i])
            for j in range(i+1,n):
                rank2 = len(hashmap[j])
                rank = rank1+rank2
                if i in hashmap[j]:
                    rank -= 1
                maxNetwork = max(maxNetwork,rank)
        
        return maxNetwork


        
        