class Solution:
    def partition(self, s: str) -> List[List[str]]:

        result = []

        def palindrome(string):
            i,j = 0,len(string)-1
            while i <= j:
                if string[i] != string[j]:
                    return False
                i += 1
                j -= 1
            return True

        def store(path):
            flag = False
            for string in path:
                if not palindrome(string):
                    flag = True
                    break
            if not flag:
                result.append(path)
        
        def backtrack(s,path):
            if not s:
                store(path[:])
                return

            for i in range(1,len(s)+1):
                path.append(s[:i])
                backtrack(s[i:],path)
                path.pop()
        
        backtrack(s,[])
        return result
