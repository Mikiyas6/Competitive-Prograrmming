class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        hashmap = defaultdict(list)

        for u, v in trust:
            hashmap[u].append(v)

        flag = False
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i != j and i not in hashmap[j]:
                    flag = True
                    break
            if not flag and not hashmap[i]:
                return i
            flag = False
        
        return -1

    
