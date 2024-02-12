class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:

        my_coordinate = [0,0]

        distance_in_x_direction = abs(my_coordinate[0] - target[0])

        distance_in_y_direction = abs(my_coordinate[1] - target[1])

        distance_from_me_to_target = distance_in_x_direction + distance_in_y_direction

        for coordinate in ghosts:

            distance_in_x_direction = abs(coordinate[0] - target[0])

            distance_in_y_direction = abs(coordinate[1] - target[1])

            distance_from_ghost_to_target = distance_in_x_direction + distance_in_y_direction

            if distance_from_ghost_to_target <= distance_from_me_to_target:

                return False
        
        return True

            

