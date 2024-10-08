class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums):

            n = len(nums)
            if n <= 1:
                return nums
            
            mid = n//2
            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])

            return merge(left,right)
        
        def merge(left,right):
            nLeft = len(left)
            nRight = len(right)
            i,j = 0, 0
            sortedArray = []

            while i < nLeft and j < nRight:
                if left[i] <= right[j]:
                    value = left[i]
                    i += 1
                else:
                    value = right[j]
                    j += 1
                sortedArray.append(value)
            
            sortedArray.extend(left[i:])
            sortedArray.extend(right[j:])

            return sortedArray
        
        return mergeSort(nums)


            
