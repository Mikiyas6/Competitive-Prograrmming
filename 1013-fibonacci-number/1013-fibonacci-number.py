class Solution:
    def fib(self, n: int) -> int:
        hashmap = defaultdict(int)  
        def fun(n):
            if n <= 1:
                return n

            if hashmap[n]:
                return hashmap[n]
            
            hashmap[n] = fun(n-1) + fun(n-2)
            
            return hashmap[n]

        return fun(n)