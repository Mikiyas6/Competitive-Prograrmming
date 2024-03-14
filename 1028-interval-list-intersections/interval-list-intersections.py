class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        n1, n2 = len(firstList), len(secondList)
        
        pointer1, pointer2 = 0, 0

        output = []

        while pointer1 < n1 and pointer2 < n2:

            s1, e1 = firstList[pointer1]
            s2, e2 = secondList[pointer2]

            if e1 >= s2 and e2 >= s1:

                s3 = max(s1,s2)
                e3 = min(e1,e2)

                output.append([s3,e3])
            
            if e2 > e1:

                pointer1 += 1
            
            elif e2 < e1:

                pointer2 += 1
            
            else:

                pointer1 += 1
                pointer2 += 1

        return output



