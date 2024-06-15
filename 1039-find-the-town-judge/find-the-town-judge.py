class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        hashmap = defaultdict(list)

        for u, v in trust:
            hashmap[u].append(v)
        
        possible = []
        for i in range(1,n+1):
            if not hashmap[i]:
                possible.append(i)
        
        flag = False
        for value in possible:
            for keys in hashmap:
                if value != keys and value not in hashmap[keys]:
                    flag = True
                    break
            if not flag:
                return value
        
        return -1

        # flag = False
        # for i in range(1,n+1):
        #     for j in range(1,n+1):
        #         if i != j and i not in hashmap[j]:
        #             flag = True
        #             break
        #     if not flag and not hashmap[i]:
        #         return i
        #     flag = False
        
        # return -1

    
