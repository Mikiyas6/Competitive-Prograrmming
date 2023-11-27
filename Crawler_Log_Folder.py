class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        stack = []

        for value in logs:

            if value == "../":

                if stack:

                    stack.pop()
            
            elif value == "./":

                continue
            
            else:

                stack.append(value)

        return len(stack)
