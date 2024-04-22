class Solution:
    def hIndex(self, citations: List[int]) -> int:

        n = len(citations)
        
        def binary_search(s,e):

            if s > e:
                return n-s
            
            mid = s + (e-s)//2
            length = n-mid
            if citations[mid] == length:
                return length
            elif citations[mid] < length:
                s = mid + 1
            else:
                e = mid - 1
            
            return binary_search(s, e)
        
        return binary_search(0,n-1)
            
        

