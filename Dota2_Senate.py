class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        n = len(senate)

        R_Queue = deque()
        D_Queue = deque()

        for i in range(n):

            if senate[i] == "R":

                R_Queue.append(i)
            
            else:

                D_Queue.append(i)

        while R_Queue and D_Queue:

            r, d = R_Queue.popleft(), D_Queue.popleft()

            if r < d:

                R_Queue.append(r+n)
            
            else:

                D_Queue.append(d+n)

        return "Radiant" if R_Queue else "Dire"
