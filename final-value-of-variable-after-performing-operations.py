class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:

        counter = 0
        
        for expression in operations:

            if expression == "--X" or expression == "X--":

                counter -= 1
            
            else:

                counter += 1
            
        return counter
