class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        output = []
        
        for i in range(len(boxes)):

            distance = 0

            for j in range(len(boxes)):

                box1 = int(boxes[i])
                box2 = int(boxes[j])

                if i != j and box2 != 0:

                    distance += abs(j - i)
            
            output.append(distance)

        return output