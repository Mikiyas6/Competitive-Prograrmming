class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        hashmap = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        combinations = []

        def dfs(digits,combo):

            if len(digits) == 0:
                com = combo[:]
                com = ''.join(combo)
                combinations.append(com)
                return
            
            for letter in hashmap[digits[0]]:

                combo.append(letter)
                dfs(digits[1:],combo)
                combo.pop()
        
        dfs(digits,[])

        return combinations

