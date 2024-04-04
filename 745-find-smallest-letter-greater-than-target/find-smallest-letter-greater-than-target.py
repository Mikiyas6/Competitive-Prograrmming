class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        def ceil(s,e,target):
    
            if s > e:
                
                return s % len(letters)
            
            mid = (s+(e-s)//2)
            
            if target < letters[mid]:
                
                e = mid-1
            
            else:
                
                s = mid+1
            
            return ceil(s,e,target)
        
        return letters[ceil(0,len(letters)-1,target)]
        

