class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()

        total = 0

        i = 0
        j = len(people) - 1

        while i < j:

            if people[i] + people[j] <= limit:

                i += 1
            
            total += 1

            j -= 1
        
        return total if i != j else total + 1