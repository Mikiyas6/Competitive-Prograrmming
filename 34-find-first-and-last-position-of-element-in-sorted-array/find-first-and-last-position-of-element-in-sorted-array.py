class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        ans = -1
        s,e = 0, len(nums)-1

        def fun(s,e,ans,side):
            
            if s > e:

                return ans
            
            mid = s + (e-s)//2

            if target < nums[mid]:

                e = mid - 1
            
            elif target > nums[mid]:

                s = mid + 1
            
            else:

                ans = mid

                if side == "left":

                    e = mid - 1
                
                else:

                    s = mid + 1
        
            return fun(s,e,ans,side)
        
        starting = fun(s,e,ans,"left")
        ending = fun(s,e,ans,"right")

        return [starting,ending]
        
        
        
            
            

