class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        dictionary = {")":"(", "]":"[", "}":"{"}

        for character in s:

            if character in dictionary.values():

                stack.append(character)
            
            elif not stack:
                
                return False
            
            else:

                if stack[-1] == dictionary[character]:
                    stack.pop()

                else:
                    return False
            
        if not stack:
            return True
            
        else:
            False

