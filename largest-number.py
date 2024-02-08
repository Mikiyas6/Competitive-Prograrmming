class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
    # Custom sorting function
        def compare(x, y):
            return int(y + x) - int(x + y)

        # Convert integers to strings
        nums_str = [str(num) for num in nums]

        # Sort the numbers using the custom sorting function
        nums_str.sort(key=cmp_to_key(compare))

        # Concatenate the sorted strings to form the largest number
        largest_num = ''.join(nums_str)

        # If the largest number is '0' at the beginning, return '0'
        return largest_num if largest_num[0] != '0' else '0'
