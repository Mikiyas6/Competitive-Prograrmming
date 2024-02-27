class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        def count_digits(num):
            count = Counter()
            while num > 0:
                count[num % 10] += 1
                num //= 10
            return count
        
        count_n = count_digits(n)
        power_of_two = 1
        for _ in range(31):  # We only need to check up to 2^31
            count_power = count_digits(power_of_two)
            if count_power == count_n:
                return True
            power_of_two <<= 1
        return False