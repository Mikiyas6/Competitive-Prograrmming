class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()  # Sort the array first
        n = len(nums)

        for x in range(1, n + 1):
            # Count how many numbers are greater than or equal to x
            count = sum(num >= x for num in nums)

            if count == x:
                return x

        return -1  # If no such x is found, return -1