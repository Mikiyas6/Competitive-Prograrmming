class Solution:
    def sumOfThree(self, num: int) -> List[int]:

        if num % 3 == 0:

            middle = num // 3

            return [middle-1,middle,middle+1]
        
        
