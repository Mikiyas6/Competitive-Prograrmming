class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        def find_ceil(s,e,target):
    
            while s <= e:
                
                mid = s + (e-s)//2
                
                if target < letters[mid]:
                    e = mid - 1
                else:
                    s = mid + 1
            
            return s
        
        def find_ceils(s,e,target):

            if s > e:
                return s
            
            mid = s + (e-s)//2

            if target < letters[mid]:
                e = mid-1
            else:
                s = mid+1
            
            return find_ceil(s,e,target)
        n = len(letters)
        index = find_ceils(0,n-1,target)
        if index < 0 or index >= n:
            index = 0
        return letters[index]
        

