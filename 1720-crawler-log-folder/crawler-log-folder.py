class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        stack = []
        counter = 0

        for char in logs:

            if char == "../":
                
                if stack:
                    stack.pop()
                    counter -= 1
            
            elif char == "./":

                continue
            
            else:

                stack.append(char)
                counter += 1
        
        return counter