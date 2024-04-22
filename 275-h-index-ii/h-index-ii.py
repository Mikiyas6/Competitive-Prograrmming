class Solution:
    def hIndex(self, citations: List[int]) -> int:

        n = len(citations)
        
        def binary_search(s,e):

            if s > e:
                return n-s
            
            mid = s + (e-s)//2
            if citations[mid] == n - mid:
                return n - mid
            elif citations[mid] < n - mid:
                s = mid + 1
            else:
                e = mid - 1
            
            return binary_search(s, e)
        
        return binary_search(0,n-1)
            
        

