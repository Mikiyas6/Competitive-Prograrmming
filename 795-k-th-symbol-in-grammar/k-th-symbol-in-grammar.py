# class Solution:
#     def kthGrammar(self, n: int, k: int) -> int:

#         def fun(grammar,counter):

#             if counter == n:
#                 return grammar
            
#             new_grammar = []
#             for value in grammar:
#                 if value == 0:
#                     option = [0,1]
#                 else:
#                     option = [1,0]

#                 new_grammar.extend(option)
            
#             return fun(new_grammar[:k+1],counter+1)

#         result = fun([0],1)

#         return result[k-1]

        
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # Base case
        if n == 1:
            return 0
        
        # Recursively calculate the value of the parent node
        parent_val = self.kthGrammar(n - 1, (k + 1) // 2)
        
        # Determine the value of the k-th element based on the parent node value
        if parent_val == 0:
            return 0 if k % 2 == 1 else 1
        else:
            return 1 if k % 2 == 1 else 0


        

        