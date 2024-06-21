class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        # Step 1: Calculate the initial satisfied customers
        initial_satisfied = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                initial_satisfied += customers[i]
        
        # Step 2: Calculate the maximum additional customers we can satisfy using the secret technique
        max_additional_satisfied = 0
        current_additional_satisfied = 0
        
        # Initialize the window
        for i in range(minutes):
            if grumpy[i] == 1:
                current_additional_satisfied += customers[i]
        
        max_additional_satisfied = current_additional_satisfied
        
        # Slide the window across the entire array
        for i in range(minutes, len(customers)):
            if grumpy[i] == 1:
                current_additional_satisfied += customers[i]
            if grumpy[i - minutes] == 1:
                current_additional_satisfied -= customers[i - minutes]
            
            max_additional_satisfied = max(max_additional_satisfied, current_additional_satisfied)
        
        # Step 3: Combine both results
        return initial_satisfied + max_additional_satisfied
