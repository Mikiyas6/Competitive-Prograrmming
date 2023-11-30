class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        string = ""

        for character in path + "/":

            if character == "/":

                if string == "..":

                    if stack:

                        stack.pop()
                
                elif string and string  != "." and string != "..":

                    stack.append(string)
                
                string = ""
            
            else:

                string += character

        return "/" + "/".join(stack)
