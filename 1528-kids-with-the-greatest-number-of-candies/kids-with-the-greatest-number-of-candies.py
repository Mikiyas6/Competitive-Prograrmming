class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        greatest_number_of_candy = max(candies)

        output = []

        for candy in candies:

            if candy + extraCandies >= greatest_number_of_candy:

                output.append(True)
            
            else:

                output.append(False)
        
        return output