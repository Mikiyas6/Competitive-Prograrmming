class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        left_over = 1

        for i in range(len(digits)-1,-1,-1):

            total = left_over + digits[i]

            if len(str(total)) > 1:

                print(int(str(total)[-1]),int(str(total)[0]))

                digits[i] = int(str(total)[-1])

                left_over = int(str(total)[0])
                
            else:

                digits[i] = total

                return digits
        
        return [left_over] + digits





