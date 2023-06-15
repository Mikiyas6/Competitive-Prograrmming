class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = [len(temperatures)-1]
        lists = [0] * len(temperatures)
        length = len(temperatures) -1
        i = len(temperatures) - 2
        while i >= 0:
            if temperatures[i] >= temperatures[stack[-1]]:
                while temperatures[i] >= temperatures[stack[-1]]:
                    stack.pop()
                    if len(stack) == 0:
                        break
                if len(stack) == 0:
                    lists[i] = 0
                    stack.append(i)
                else:
                    lists[i] = stack[-1] - i
                    stack.append(i)
            elif temperatures[i] < temperatures[stack[-1]]:
                lists[i] = stack[-1] - i
                stack.append(i)
            i -= 1
        return lists
