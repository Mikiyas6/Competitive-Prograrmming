class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        string1 = ""
        string2 = ""
        
        for letter in s:

            if letter != "#":

                string1 += letter
            
            else:

                string1 = string1[:len(string1)-1]
        
        for letter in t:

            if letter != "#":

                string2 += letter
            
            else:

                string2 = string2[:len(string2)-1]
        
        return True if string1 == string2 else False




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

