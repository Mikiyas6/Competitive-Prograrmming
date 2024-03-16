class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:

        def isPalindrome(string: str) -> bool:

            i = 0
            j = len(string) - 1

            while i <= j:

                if string[i] != string[j]:

                    return False
                
                i += 1
                j -= 1
                
            return True

        def checker(a,b):

            i = 0
            j = n - 1

            while i <= j:

                if a[i] != b[j]:

                    break
                
                i += 1
                j -= 1
            
            if i >= j:

                return True
            
            return isPalindrome(a[i:j+1]) or isPalindrome(b[i:j+1])
        
        n = len(a)

        return checker(a,b) or checker(b,a)

        

             
        
        # n = len(a)

        # def isPalindrome(string: str) -> bool:

        #     i = 0
        #     j = len(string) - 1

        #     while i <= j:

        #         if string[i] != string[j]:

        #             return False
                
        #         i += 1
        #         j -= 1
                
        #     return True
        
        # pointer = 0

        # while pointer <= n:

        #     a_prefix = a[:pointer]
        #     a_suffix = a[pointer:]

        #     b_prefix = b[:pointer]
        #     b_suffix = b[pointer:]

        #     string1 = a_prefix + b_suffix
        #     string2 = b_prefix + a_suffix

        #     if isPalindrome(string1) or isPalindrome(string2):

        #         return True
            
        #     pointer += 1
        




        

        