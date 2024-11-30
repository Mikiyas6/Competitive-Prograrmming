class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
        
        hashmap = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        result = []
        def backtrack(i,path):
            if i == len(digits):
                result.append(''.join(path[:]))
                return
            letters = hashmap[digits[i]]
            for j in range(len(letters)):
                path.append(letters[j])
                backtrack(i+1,path)
                path.pop()
        backtrack(0,[])
        return result
            

        