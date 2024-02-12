# class Solution:
#     def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:

#         max_row = 0
#         max_column = 0

#         for row, column in ghosts + [target]:

#             max_row = max(max_row,row)
#             max_column = max(max_column,column)

#         size = max(max_row,max_column)

#         def inbound(coordinate):

#             return coordinate[0] > -1 and coordinate[0] < size and coordinate[1] > -1 and coordinate[1] < size
        
#         def dfs(coordinate,counter):

#             if not inbound(coordinate) or coordinate == target:

#                 return counter
            
#             if inbound(coordinate):

#                 direction_1 = dfs([coordinate[0]-1,coordinate[1]], counter+1)
#                 direction_2 = dfs([coordinate[0]+1,coordinate[1]], counter+1)
#                 direction_3 = dfs([coordinate[0],coordinate[1]-1], counter+1)
#                 direction_4 = dfs([coordinate[0],coordinate[1]+1], counter+1)
            
#             return min([direction_1,direction_2,direction_3,direction_4])
        
#         min_distance = float("inf")

#         for coordinate in ghosts:

#             print(coordinate)

#             min_distance = min(min_distance,dfs(coordinate,0))
        
#         mine = dfs([0,0],counter,0)

#         return True if mine < min_distance else False

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        for ghost in ghosts:
            distance_apart_x = abs(target[0] - ghost[0])
            distance_apart_y = abs(target[1] - ghost[1])
            distance_apart = distance_apart_x + distance_apart_y
            target_distance = abs(target[0]) + abs(target[1])
            
            if (distance_apart <= target_distance):
                return False
            
        return True