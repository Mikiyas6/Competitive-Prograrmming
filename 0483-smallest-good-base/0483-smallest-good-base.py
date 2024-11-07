class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        max_length = math.ceil(math.log(n, 2)) + 1

        def good(k):
            
            l, r = 2, n
            while l < r:
                mid = (l + r) // 2
                total = 0
                for j in range(k):
                    total += mid ** j
                
                if total == n:
                    return mid
                
                elif total > n:
                    r = mid - 1
                
                elif total < n:
                    l = mid + 1

            total = 0
            for j in range(k): 
                total += l ** j
            if total == n:
                return l

            return 0
        
        for sol_length in range(max_length, 1, -1):
            if val := good(sol_length):
                return str(val)
        
        return str(n - 1)



        

    
            