class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        lists = []

        skill.sort()

        i = 0
        j = len(skill) - 1
    
        if len(skill) == 2:
            return skill[0] * skill[1]

        while i < j:

            if i == 0:

                lists.append([skill[i],skill[j]])
            
            else:

                if sum([skill[i],skill[j]]) != sum( lists[-1]):
                    return -1
                lists.append([skill[i],skill[j]])

            i += 1
            j -= 1
        
        total = 0
        
        for team in lists:

            total += team[0] * team[1]

        return total


            
