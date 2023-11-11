class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:

        total = 0
        
        for value in hours:

            if value >= target:
                
                total += 1
        
        return total
