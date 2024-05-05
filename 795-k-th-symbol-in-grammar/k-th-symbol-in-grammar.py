class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        def fun(n,k):
            # Base case
            if n == 1:
                return 0
            
            # Recursively calculate the value of the parent node
            parent_node_value = fun(n - 1, (k + 1) // 2)
            
            # Determine the value of the k-th element based on the parent node value
            if parent_node_value == 0:
                return 0 if k % 2 == 1 else 1
            else:
                return 1 if k % 2 == 1 else 0
        
        return fun(n,k)


        

        