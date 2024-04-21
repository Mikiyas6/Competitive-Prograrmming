class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        def binary_search(s,e,nums,target):
           
            while s <= e:

                mid = s + (e-s)//2

                if target > nums[mid]:

                    s = mid+1
                
                elif target < nums[mid]:

                    e = mid - 1
                
                else:

                    return mid
                
            return -1

        n = len(numbers)

        for index, value in enumerate(numbers):

            diff = target - value

            result = binary_search(index+1,n-1,numbers,diff)

            if result != -1:

                return [index+1,result+1]

        # while s != e:

        #     total = numbers[s] + numbers[e]

        #     if total > target:

        #         e -= 1
            
        #     elif total < target:

        #         s += 1
            
        #     else:

        #         return [s+1,e+1]

        
            