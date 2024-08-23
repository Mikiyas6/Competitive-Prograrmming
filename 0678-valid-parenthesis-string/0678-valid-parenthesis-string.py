class Solution:
    def checkValidString(self, s: str) -> bool:
        
        stack_left = []
        stack_star = []
        for i, char in enumerate(s):
            if char == '(':
                stack_left.append(i)
            elif char == '*':
                stack_star.append(i)
            else:
                if stack_left:
                    stack_left.pop()
                elif stack_star:
                    stack_star.pop()
                else:
                    return False
        while stack_left and stack_star:
            if stack_left[-1] < stack_star[-1]:
                stack_left.pop()
                stack_star.pop()
            else:
                break
        return len(stack_left) == 0