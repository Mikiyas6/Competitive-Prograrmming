class Solution:
    def smallestNumber(self, num: int) -> int:
        
        new_nums = list(map(str,str(num)))

        sign = ""

        if new_nums[0] == "-":

            sign = new_nums[0]

            new_nums = new_nums[1:]
        
        final = list(map(int,new_nums))

        final.sort()

        if sign:

            final = final[::-1]
        
        else:

            for index,value in enumerate(final):

                if value:

                    value = final.pop(index)
                    break
            
            final = [value] + final

        string = list(map(str,final))
        
        string = "".join(string)

        string = sign + string

        return int(string)
        