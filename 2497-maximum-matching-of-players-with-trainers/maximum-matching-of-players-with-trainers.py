class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:

        players.sort()
        trainers.sort()

        n, m = len(players), len(trainers)

        i, j, counter = 0, 0, 0
        
        while i < n and j < m:

            if players[i] <= trainers[j]:

                    counter += 1

                    i += 1
            
            j += 1
        
        return counter


            