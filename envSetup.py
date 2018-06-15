import numpy as np


#
class EnvSetup():
    #
    def __init__(self):
        # Map parameters -- USER CUSTOMERIZED.
        self.map_width = 30
        self.map_height = 15
        
        # Define sub_walls. -- USER CUSTOMERIZED.
        # sub_block of the whole wall -> sub_wall.
        # pos_sub_wall = [[(xmin, xmax), (ymin, ymax)],
        #                 [(xmin, xmax), (ymin, ymax)], ...]
        pos_sub_wall = []
        pos_sub_wall.append([(3, 4), (3, 11)])
        pos_sub_wall.append([(13, 14), (0, 3)])
        pos_sub_wall.append([(21, 25), (8, 9)])
        pos_sub_wall.append([(21, 22), (10, 14)]) 
        
        # Robot -- USER CUSTOMERIZED.
        self.n_robot = 20
        self.n_target = 1
        
        # 
        self.nodes_all = self.map_generator(self.map_width, self.map_height)
        self.nodes_wall = self.wall_generator(pos_sub_wall)
        self.nodes_movable = self.movableNodes_generator()

    
    
    # Generate the map.
    def map_generator(self, width, height):
        pos_all = [];
        for x in range(width):
            for y in range(height):
                pos_all.append([x, y])
                
        return pos_all
    
    
  
    # Generate the wall.
    def wall_generator(self, pos_sub_wall): 
        # Construct the positions of the wall.
        pos_wall = []
        for index_sub_wall in np.arange(len(pos_sub_wall)):
            for index_x in np.arange(pos_sub_wall[index_sub_wall][0][0], pos_sub_wall[index_sub_wall][0][1] + 1):
                for index_y in np.arange(pos_sub_wall[index_sub_wall][1][0], pos_sub_wall[index_sub_wall][1][1] + 1):
                    pos_wall.append([index_x, index_y])     
        
        return pos_wall
    
    
    # Generate the movable positions/nodes.
    def movableNodes_generator(self):
        pos_movable = [pos for pos in self.nodes_all if pos not in self.nodes_wall]
        return pos_movable
    
    
    