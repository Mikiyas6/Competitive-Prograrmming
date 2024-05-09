# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        def find_first_and_last(s,e,ans,isFirst,isAsc):
            
            if s > e:
                return ans
            
            mid = s + (e-s)//2
            if isAsc:

                if target < mountain_arr.get(mid):
                    e = mid-1
                elif target > mountain_arr.get(mid):
                    s = mid+1
                else:
                    ans = mid

                    if isFirst:
                        e = mid-1
                    else:
                        s = mid+1
            else:

                if target > mountain_arr.get(mid):
                    e = mid-1
                elif target < mountain_arr.get(mid):
                    s = mid+1
                else:
                    ans = mid

                    if isFirst:
                        e = mid-1
                    else:
                        s = mid+1

            
            return find_first_and_last(s,e,ans,isFirst,isAsc)

        def find_peak_element(s,e):

            if s == e:
                return s
            
            mid = s + (e-s)//2
            if mountain_arr.get(mid) < mountain_arr.get(mid+1):
                s = mid+1
            else:
                e = mid

            return find_peak_element(s,e)
         
        s, e = 0, mountain_arr.length()-1
        peak_index = find_peak_element(s,e)

        if target == mountain_arr.get(peak_index):
            return peak_index

        s, e = 0, peak_index-1
        ans = -1

        first_left = find_first_and_last(s,e,ans,True,True)

        if first_left > -1:
            return first_left

        ans = -1
        s, e = peak_index+1, mountain_arr.length()-1
        first_right = find_first_and_last(s,e,ans,True,False)

        return first_right