class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        hashmap_count = defaultdict(int)
        hashmap_streaks = defaultdict(int)

        for winner, loser in matches:

            hashmap_count[winner] += 1
            hashmap_count[loser] += 1

            hashmap_streaks[winner] += 1
            hashmap_streaks[loser] -= 1
        
        havent_lost = []
        lost_one = []
        
        for value in hashmap_count:

            if hashmap_count[value] == hashmap_streaks[value]:

                havent_lost.append(value)
            
            elif hashmap_count[value] - 2 == hashmap_streaks[value]:

                lost_one.append(value)
        
        havent_lost.sort()
        lost_one.sort()
        
        return [havent_lost,lost_one]
