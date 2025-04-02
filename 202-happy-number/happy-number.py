class Solution:
    def isHappy(self, n: int) -> bool:
        # hashset = set([0])
        # while n != 1:
        #     temp = n
        #     total = 0
        #     while temp != 0:
        #         total +=  (temp%10)**2
        #         temp //= 10
        #     if total in hashset:
        #         return False
        #     n = total
        #     hashset.add(total)
        # return True
        if n == 1:
            return True
        def sum_of_squares(n):
            temp = n
            total = 0
            while temp != 0:
                total += (temp%10)**2
                temp //= 10
            return total
        slow = n
        fast = sum_of_squares(n)
        while slow != fast:
            slow = sum_of_squares(slow)
            fast = sum_of_squares(sum_of_squares(fast))
            if slow == 1:
                return True
        return False
            
