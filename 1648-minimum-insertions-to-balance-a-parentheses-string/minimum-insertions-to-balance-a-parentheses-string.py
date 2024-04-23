class Solution:
    def minInsertions(self, s: str) -> int:
        
        stack = []
        counter = 0
        n = len(s)
        index = 0

        while index < n:

            if s[index] == "(":
                stack.append(s[index])
                index += 1
            
            else:

                if not stack:

                    if index+1 < n and s[index+1] == ")":
                        counter += 1
                        index += 2
                    else:
                        counter += 2
                        index += 1

                else:
                    if index+1 < n and s[index+1] == ")":
                        index += 2
                    else:
                        index += 1
                        counter += 1
                    stack.pop()

        return counter + (len(stack)*2)