class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def fun(start,end):
            if start > end:
                return
            s[start],s[end] = s[end],s[start]
            start += 1
            end -= 1
            fun(start,end)
        
        fun(0,len(s)-1)