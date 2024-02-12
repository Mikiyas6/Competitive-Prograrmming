class Solution:
    def isHappy(self, n: int) -> bool:

        def find_square(number:int) -> int:

            answer = 0

            while number > 0:

                rem = number % 10

                answer += rem ** 2

                number = number // 10
            
            return answer
        
        if n == 1:

            return True
        
        if n <= 1:

            return False

        slow = n
        fast = find_square(find_square(n))

        while slow != fast :

            slow = find_square(slow)
            fast = find_square(find_square(fast))

            if fast == 1:

                return True