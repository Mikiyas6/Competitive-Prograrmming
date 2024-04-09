class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        n = len(tickets)
        total_tickets = sum(tickets)
        pass_num = 0

        while tickets[k] > 0:
            for i in range(n):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    total_tickets -= 1
                    pass_num += 1
                    if i == k and tickets[i] == 0:
                        return pass_num

        return pass_num