class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Sort people by height (in decreasing order) and then by the number of people in front
        people.sort(key=lambda x: (-x[0], x[1]))
        
        queue = []
        for person in people:
            # Insert the person into the queue at the position specified by the second attribute
            queue.insert(person[1], person)
        
        return queue
