class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()

        counter = 0

        i, j = 0, len(people) - 1 

        while i < j:

            total = people[i] + people[j]

            if total <= limit:

                i += 1
                j -= 1
            
            else:

                j -= 1
            
            counter += 1
        
        return counter + 1 if i == j else counter


# class Solution:
#     def numRescueBoats(self, people: List[int], limit: int) -> int:
        
#         people.sort()
#         i = 0
#         j = len(people) - 1

#         counter = 0

#         while i < j:

#             if people[i] + people[j] <= limit:
#                 counter += 1
#                 i += 1
#                 j -= 1
            
#             else:
#                 j -= 1

#         return len(people) - counter
            
