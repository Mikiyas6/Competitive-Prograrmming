class Solution:
    def addDigits(self, num: int) -> int:
        
        string = str(num)

        while len(string) > 1:

            result = 0

            for value in string:

                result += int(value)
            
            string = str(result)
            
        return int(string)
            

