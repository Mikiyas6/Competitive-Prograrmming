class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        i = 0
        j = len(people) - 1

        counter = 0

        while i < j:

            if people[i] + people[j] <= limit:
                counter += 1
                i += 1
                j -= 1
            
            else:
                j -= 1

        return len(people) - counter
            
