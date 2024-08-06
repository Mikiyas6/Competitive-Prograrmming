class Solution:
    def climbStairs(self, n: int) -> int:
        hashmap = defaultdict(int)
        hashmap[0] = 1
        def fun(n):
            if n < 0:
                return 0
            if n in hashmap:
                return hashmap[n]
            
            value1 = fun(n-1)
            value2 = fun(n-2)
            hashmap[n] = value1 + value2
            return hashmap[n]
        
        return fun(n)

