class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        monotonic_stack = []

        result = [0] * len(temperatures)

        for index, value in enumerate(temperatures):

            while monotonic_stack and value > temperatures[monotonic_stack[-1]]:

                removed = monotonic_stack.pop()

                diff = index - removed

                result[removed] = diff
            
            monotonic_stack.append(index)
        
        return result
