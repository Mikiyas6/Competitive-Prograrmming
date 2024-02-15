class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:

        steps = 0
        original_capacity = capacity

        for index, amount in enumerate(plants):

            if capacity - amount >= 0:

                steps += 1

                capacity -= amount
            
            else:

                steps += (2 * index) + 1

                capacity = original_capacity - amount
            
        return steps

            
