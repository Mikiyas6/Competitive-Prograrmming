class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        ans, used, max_half = 0, set(), 10**((n+1)//2)
        for half in map(str, range(max_half//10, max_half)):
            num = (half[:-1:] if n%2 else half) + half[::-1]
            if int(num) % k == 0 and (mask := ''.join(sorted(num))) not in used:
                used.add(mask)
                freq, cnt = Counter(num), factorial(n)
                for f in freq.values():
                    cnt //= factorial(f)
                ans += cnt - cnt * freq['0'] // n 
        return ans