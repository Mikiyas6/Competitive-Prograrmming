class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        upper = pow(10, n) - 1
        lower = pow(10, n - 1)
        for i in range(upper, lower-1, -1):
            s = str(i)
            pal = int(s + s[::-1])
            for j in range(upper, int(pow(pal, 0.5))-1, -1):
                if pal % j == 0 and len(str(pal//j)) == n:
                    return pal % 1337
        return -1