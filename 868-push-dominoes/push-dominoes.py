class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        n = len(dominoes)
        forces_left = [0] * n
        forces_right = [0] * n

        force = 0
        for i in range(n):
            if dominoes[i] == 'R':
                force = n
            elif dominoes[i] == 'L':
                force = 0
            else:
                force = max(force - 1, 0)
            forces_right[i] = force

        force = 0
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                force = n
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(force - 1, 0)
            forces_left[i] = force

        result = ''
        for i in range(n):
            if forces_left[i] == forces_right[i]:
                result += '.'
            elif forces_left[i] < forces_right[i]:
                result += 'R'
            else:
                result += 'L'

        return result