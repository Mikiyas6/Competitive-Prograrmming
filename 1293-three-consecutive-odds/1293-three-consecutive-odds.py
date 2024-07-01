class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        if len(arr) < 3:
            return False

        for index, value in enumerate(arr):
            if value %2 != 0:
                arr[index] = 0
        
        total = sum(arr[:3])

        if total == 0:
            return True
        
        l = 0

        for r in range(3,len(arr)):
            total -= arr[l]
            total += arr[r]
            if total == 0:
                return True
            l += 1
        
        return False
