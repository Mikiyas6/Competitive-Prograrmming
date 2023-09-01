"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, target_id):
        """
        :type employees: List[Employee]
        :type target_id: int
        :rtype: int
        """
        employee_map = {employee.id: employee for employee in employees }
        
        def calculateImportance(target_id):
            total_importance = employee_map[target_id].importance
            for subordinate_id in employee_map[target_id].subordinates:
                total_importance += calculateImportance(subordinate_id)
            return total_importance
        
        return calculateImportance(target_id)


        
