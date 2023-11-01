class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []
        current = ""
        path = path + "/"
        
        for char in path:

            if char == "/":

                if current == "..":
                    if stack:
                        stack.pop()
                
                elif current != "." and current != "":
                    stack.append(current)
                
                current = ""
            
            else:

                current += char
        
        return "/" + "/".join(stack)
