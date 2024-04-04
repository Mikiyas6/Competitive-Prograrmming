class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        def ceil(s,e,target):
    
            if s > e:
                
                return s
            
            mid = (s+(e-s)//2)
            
            if target < letters[mid]:
                
                e = mid-1
            
            else:
                
                s = mid+1
            
            return ceil(s,e,target)
        
        index = ceil(0,len(letters)-1,target)

        if index < 0 or index >= len(letters):

            index = 0
        
        return letters[index]
        

