class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        result = [0]*len(temperatures)

        for index, value in enumerate(temperatures):

            while stack and value > temperatures[stack[-1]]:

                idx = stack.pop()

                result[idx] = index - idx
            
            stack.append(index)
        
        return result