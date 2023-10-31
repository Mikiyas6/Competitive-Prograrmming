class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        stack = []

        for moves in logs:

            if moves == "../" and stack:
                stack.pop()
            
            elif moves == "./":
                continue
            
            elif moves != "../" and moves != "./":
                stack.append(moves)
        
        return len(stack)
                
