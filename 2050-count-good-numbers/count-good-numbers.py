class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = (10**9) + 7
        even_position = n//2 + n%2
        odd_position = n//2
        def find_power(position,power):
            if power == 0:
                return 1
            if power == 1:
                return position
            result = find_power(position,power//2)
            return (result * result * (position**(power%2)))%MOD
        return (find_power(5,even_position) * find_power(4,odd_position)) % MOD