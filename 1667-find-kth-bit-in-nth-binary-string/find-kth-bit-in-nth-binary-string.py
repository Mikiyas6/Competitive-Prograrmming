class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def invert(string):

            if not string:
                return string
            
            result = []
            for char in string:
                if char == "1":
                    value = "0" 
                else:
                    value = "1"
                result.append(value)
            return "".join(result)
        
        def reverse(string):

            i = 0
            j = len(string)-1
            string = list(string)

            while i < j:
                string[i],string[j] = string[j],string[i]
                i += 1
                j -= 1
            return "".join(string)
        
        def fun(n):

            if n <= 1:
                return "0"
            
            previous = fun(n-1)
            return  previous + "1" + reverse(invert(previous))
        return fun(n)[k-1]