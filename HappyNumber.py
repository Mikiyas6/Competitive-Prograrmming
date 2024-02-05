class Solution:
    def isHappy(self, n: int) -> bool:

        if n == 1 or n == 7:

            return True

        if n <= 9:

            return False

        result = n
        
        while result != 1:

            string = str(result)

            output = 0

            for value in string:

                output += int(value) ** 2
            
            result = output
            
            if result == 1 or result == 7:

                return True

            if result == n or result <= 9:

                return False
        
        return True
