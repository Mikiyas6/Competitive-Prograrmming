class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        players = list(range(1,n+1))

        counter = n

        loser = 0

        while counter != 1:

            loser += k-1

            loser %= counter

            players.pop(loser)

            counter -= 1
        
        return players[0]

            