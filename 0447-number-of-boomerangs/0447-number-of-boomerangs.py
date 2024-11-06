class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        boomerangs = 0
        for p1 in points:
            distances = defaultdict(int)
            for p2 in points:
                if p1 == p2:
                    continue
                dist = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
                distances[dist] += 1
            for dist in distances.values():
                boomerangs += dist * (dist - 1)
        return boomerangs