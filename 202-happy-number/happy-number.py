class Solution:
    def isHappy(self, n: int) -> bool:
        
        visited = []

        def fun(n):

            if n == 1:

                return True
            
            if n in visited:

                return False
            
            visited.append(n)
            string = str(n)
            new_n = 0

            for value in string:

                new_n += int(value) ** 2
            
            n = new_n

            return fun(n)
        
        return fun(n)

