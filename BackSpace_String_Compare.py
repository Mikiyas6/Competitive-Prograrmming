class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        string1 = ""
        size = 0

        for character in s:

            if character == "#":

                string1 = string1[:size-1]
                size = 0 if size == 0 else size - 1
            
            else:

                string1 += character
                size += 1
        
        string2 = ""
        size = 0

        for character in t:

            if character == "#":

                string2 = string2[:size-1]

                size = 0 if size == 0 else size - 1
            
            else:

                string2 += character
                size += 1

        return string1 == string2

        





# class Solution:
#     def backspaceCompare(self, s: str, t: str) -> bool:
        
#         stack = []

#         for char in s:

#             print(stack)

#             if char == "#": 
#                 if stack:
#                     stack.pop()
#             else:

#                 stack.append(char)
        
#         string = "".join(stack)


#         stack = []


#         for char in t:

#             if char == "#":
#                 if stack:
#                     stack.pop()
            
#             else:

#                 stack.append(char)
                

#         if string == "".join(stack):
#             return True
        
#         return False

