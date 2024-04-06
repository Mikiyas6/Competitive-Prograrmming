class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        def binary_search(s,e,nums,target):

            if s > e:

                return -1
            
            mid = s + (e-s)//2

            if nums[mid] == target:

                return mid
            
            elif target > nums[mid]:

                s = mid + 1
            
            else:

                e = mid - 1
            
            return binary_search(s,e,nums,target)

        n = len(numbers)

        for index, value in enumerate(numbers):

            diff = target - value

            result = binary_search(index+1,n-1,numbers,diff)

            if result != -1:

                return [index+1,result+1]
        
        # left, right = 0, len(numbers) - 1

        # while left != right:

        #     total = numbers[left] + numbers[right]

        #     if total > target:

        #         right -= 1
            
        #     elif total < target:

        #         left += 1
            
        #     else:

        #         return [left+1,right+1]

        
            