class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        if len(a) > len(b):

            diff = len(a) - len(b)

            b = "0"*diff + b
        
        elif len(b) > len(a):

            diff = len(b) - len(a)

            a = "0"*diff + a
        
        carry = 0

        string = ""
        
        for i in range(len(a)-1,-1,-1):

            opperand_a = int(a[i])
            opperand_b = int(b[i])

            result = opperand_a + opperand_b + carry

            if result == 0:

                string += "0"

                carry = 0
            
            elif result == 1:

                string += "1"

                carry = 0

            elif result == 2:

                string += "0"

                carry = 1
            
            elif result == 3:

                string += "1"

                carry = 1
        
        if carry:

            string += str(carry)
        
        string = string[::-1]

        return string
            
            



