class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        student_queue = deque(students)
        sandwich_stack = sandwiches[::-1]  
        unable_to_eat = 0

        while student_queue:
            if student_queue[0] == sandwich_stack[-1]:
                student_queue.popleft()
                sandwich_stack.pop()
                unable_to_eat = 0  
            else:
                student_queue.append(student_queue.popleft())
                unable_to_eat += 1

            if unable_to_eat == len(student_queue):
                return unable_to_eat

        return unable_to_eat