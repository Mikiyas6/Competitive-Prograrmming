class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        pair1,pair2 = edges[0]
        for i in range(1,len(edges)):
            if pair1 in edges[i]:
                return pair1
            else:
                return pair2
