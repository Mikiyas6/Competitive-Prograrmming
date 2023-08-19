class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        Graph = defaultdict(set)
        for city1, city2 in roads:
            Graph[city1].add(city2)
            Graph[city2].add(city1)
        result = 0
        for city1,city2 in itertools.combinations(Graph.keys(),2):
            has_connection = 1 if city1 in Graph[city2] else 0

            city1_connection = len(Graph[city1])
            city2_connection = len(Graph[city2])

            result = max(result, city1_connection + city2_connection - has_connection)
        return result
