class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        num_rooms = len(rooms)
        visited_rooms = [False] * num_rooms
        stack = [0]
        visited_rooms[0] = True
        visited_count = 0

        while stack:
            current_room = stack.pop()
            visited_count += 1

            for next_room in rooms[current_room]:
                if not visited_rooms[next_room]:
                    visited_rooms[next_room] = True
                    stack.append(next_room)

        return visited_count == num_rooms