class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(a,b): return (a[0]-b[0])**2+(a[1]-b[1])**2
        arr=sorted([(dist(p1,p2),p2),(dist(p1,p3),p3),(dist(p1,p4),p4),])
        return dist(arr[0][1],arr[1][1])==arr[2][0] and arr[0][0]==arr[1][0]==dist(arr[0][1],arr[2][1])==dist(arr[1][1],arr[2][1])!=0