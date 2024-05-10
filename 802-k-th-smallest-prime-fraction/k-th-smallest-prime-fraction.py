class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        
        n = len(arr)
        left, right = 0.0, 1.0

        while left < right:
            mid = (left + right) / 2
            count = 0
            max_fraction = [0, 1]

            # Count the number of fractions <= mid
            j = 1
            for i in range(n - 1):
                while j < n and arr[i] / arr[j] > mid:
                    j += 1
                count += n - j
                if j < n and max_fraction[0] * arr[j] < arr[i] * max_fraction[1]:
                    max_fraction = [arr[i], arr[j]]

            if count == k:
                return max_fraction
            elif count < k:
                left = mid
            else:
                right = mid

        return []