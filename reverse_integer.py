class Solution:
    def reverse(self, x: int) -> int:
        string = str(x)
        new_string = ""
        sign = ""
        for value in string:
            if value.isdigit():
                new_string = value + new_string
            else:
                sign = value
        if sign == "-":
            new_string = sign + new_string
        if int(new_string) < -2**31 or int(new_string) > 2**31 - 1:
            return 0
        else:
            return int(new_string)
