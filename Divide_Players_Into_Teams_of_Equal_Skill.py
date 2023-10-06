class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        skill.sort()

        lists = [(skill[0],skill[len(skill)-1])]
        total = sum((skill[0],skill[len(skill)-1]))
        i = 1
        j = len(skill) - 2
        sums = 0

        if i >= j:
            return lists[0][0] * lists[0][1]

        while i < j:

            if sum((skill[i],skill[j])) != total:
                return -1

            lists.append((skill[i],skill[j]))

            i += 1
            j -= 1
        
        for value in lists:
            sums += value[0] * value[1]
        
        return sums
            
