class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binary_search(s,e,ans,position):

            if s > e:

                return ans
            
            mid = s + (e-s)//2

            if target > nums[mid]:

                s = mid + 1

            elif target < nums[mid]:

                e = mid - 1

            else:

                ans = mid

                if position == "first":

                    e = mid - 1
                
                else:

                    s = mid + 1
            
            return binary_search(s,e,ans,position)
        
        ans = -1

        s, e = 0, len(nums) - 1
        
        first = binary_search(s,e,ans,"first")

        last = binary_search(s,e,ans,"end")

        return [first,last]
            


