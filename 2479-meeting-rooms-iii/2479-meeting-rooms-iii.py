import heapq as heap
from queue import Queue
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        free_rooms = list(range(n))
        heapify(free_rooms)
        meetings_info = []
        num_rooms = [0] * n
        for start, end in sorted(meetings):
            while meetings_info and meetings_info[0][0] <= start:
                _, room_number = heappop(meetings_info)
                heappush(free_rooms, room_number)
            if free_rooms:
                room_number = heappop(free_rooms)
                heappush(meetings_info, (end, room_number))
            else:
                end_time, room_number = heappop(meetings_info)
                heappush(meetings_info, (end_time + end - start, room_number))
            num_rooms[room_number] += 1

        return num_rooms.index(max(num_rooms))