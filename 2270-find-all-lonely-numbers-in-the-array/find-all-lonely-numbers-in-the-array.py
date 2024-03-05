class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        
        num_counts = {}
        for num in nums:
            num_counts[num] = num_counts.get(num, 0) + 1

        lonely_numbers = []
        for num, count in num_counts.items():
            if count == 1 and (num - 1 not in num_counts and num + 1 not in num_counts):
                lonely_numbers.append(num)

        return lonely_numbers