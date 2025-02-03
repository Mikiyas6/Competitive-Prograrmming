class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        hashmap = defaultdict(list)
        visited = set()
        length = 0
        for winner,loser in matches:
            hashmap[loser].append(winner)
            length = max(length,max(winner,loser))
            visited.add(loser)
            visited.add(winner)
        ans1 = []
        ans2 = []
        for i in range(1,length+1):
            if i in visited and i not in hashmap.keys():
                ans1.append(i)
            if hashmap[i] and len(hashmap[i]) == 1:
                ans2.append(i)
        return [ans1,ans2]
        
        