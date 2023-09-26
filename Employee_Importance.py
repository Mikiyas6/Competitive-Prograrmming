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

        visited = set()

        dictionary = {}

        for i in range(len(employees)):
            dictionary[employees[i].id] = i

        def dfs(target_id):

            if not employees[target_id].subordinates:
                return employees[target_id].importance

            visited.add(target_id)

            total = employees[target_id].importance

            for subordinates in employees[target_id].subordinates:

                if dictionary[subordinates] not in visited:
                    visited.add(dictionary[subordinates])
                    total += dfs(dictionary[subordinates] )

            return total

        for i in range(len(employees)):
            if employees[i].id == target_id:
                return dfs(i)




        

        
