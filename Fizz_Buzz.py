class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        lists = []
        for i in range(1,n+1):
            if i%3 == 0 and i%5 == 0:
                lists.append("FizzBuzz")
            elif (i%3 == 0):
                lists.append("Fizz")
            elif (i%5 == 0):
                lists.append("Buzz")
            else:
                lists.append(str(i))
        return lists
