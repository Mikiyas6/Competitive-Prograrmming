class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        output = []
        
        for i in range(left,right+1):

            string = str(i)
            flag = True

            for value in string:

                if value == "0" or i % int(value) != 0:

                    flag = False
                    break       
            
            if flag:

                output.append(i)
        
        return output
            
