class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        string = ""

        for value in digits:

            string += str(value)

        numerical_digit = int(string)

        result = numerical_digit + 1

        string = str(result)

        lists = []

        for item in string:

            lists.append(int(item))
        
        return lists

