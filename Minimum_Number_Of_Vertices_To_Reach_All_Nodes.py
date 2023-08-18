class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # Adjacency_Matrix = [[0]*n for _ in range(n)]
        # for i in range(len(edges)):
        #     Adjacency_Matrix[edges[i][0]][edges[i][1]] = 1
        # lists = []
        # for i in range(n):
        #     flag = True
        #     for j in range(n):
        #         if Adjacency_Matrix[j][i] == 1:
        #             flag = False
        #             break
        #     if flag:
        #         lists.append(i)
        # return lists
        lists = []
        for i in range(len(edges)):
            lists.append(edges[i][1])
        lists3 = list(set([i for i in range(n)]).difference(set(lists)))
        return lists3
