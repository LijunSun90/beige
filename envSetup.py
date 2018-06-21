import numpy as np


#
class EnvSetup():
    #
    def __init__(self):
        # Fixing random state for reproducibility -- USER CUSTOMERIZED.
        self.seed = 19680801
        
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
        
        # The order of variable definition cannot be varied.
        self.nodes_all = self.map_generator(self.map_width, self.map_height)
        self.nodes_wall = self.wall_generator(pos_sub_wall)
                
        # Robot -- USER CUSTOMERIZED.
        self.n_robot = 20
        self.n_target = 1
        
        self.nodes_target_initializer = self.target_initializer(self.n_target)
        
        self.nodes_obstacleStatic = self.nodes_wall
        self.nodes_obstacleDynamic = []
        
        self.nodes_robot_initializer = self.robot_initializer(self.n_robot)
        
        self.nodes_obstacle = self.nodes_obstacleStatic + self.nodes_obstacleDynamic
        self.nodes_passable = self.passableNodes_generator()

    
    
    # Generate the map.
    def map_generator(self, width, height):
        pos_all = [];
        for x in range(width):
            for y in range(height):
                pos_all.append((x, y))
                
        return pos_all
    
    
    # Generate the wall.
    def wall_generator(self, pos_sub_wall): 
        # Construct the positions of the wall.
        pos_wall = []
        for index_sub_wall in np.arange(len(pos_sub_wall)):
            for index_x in np.arange(pos_sub_wall[index_sub_wall][0][0], pos_sub_wall[index_sub_wall][0][1] + 1):
                for index_y in np.arange(pos_sub_wall[index_sub_wall][1][0], pos_sub_wall[index_sub_wall][1][1] + 1):
                    pos_wall.append((index_x, index_y))    
        
        return pos_wall
    
    
    # Generate the passable positions/nodes.
    def passableNodes_generator(self):
        pos_passable = [pos for pos in self.nodes_all if pos not in self.nodes_obstacleStatic]
        return pos_passable
    
    
    # Generate the initial positions of the target.
    def target_initializer(self, n_target):
        # Set the initial position of  the target at the center of the map.
        pos_target = tuple(np.around((self.map_width*0.5, self.map_height*0.5)))
#         pos_target = [[round(self.map_width*0.5), round(self.map_height*0.5)]]
        return [pos_target]
    
    
    # Generate the initial positions of the robots.
    def robot_initializer(self, n_robot):
        np.random.seed(self.seed)
        pos_robots = []
        for ix in np.arange(n_robot):
            pos_robot = tuple(np.around(np.random.uniform([0, 0], [self.map_width, self.map_height], 2)))
            # Ensure the new position is not a duplicate of any previous robot's position.
            while pos_robot in (self.nodes_obstacleStatic + self.nodes_obstacleDynamic):
                pos_robot = tuple(np.around(np.random.uniform([0, 0], [self.map_width, self.map_height], 2)))
            # Add the new robot position to self.nodes_obstacleDynamic.
            self.nodes_obstacleDynamic.append(pos_robot) 
            pos_robots.append(pos_robot)
               
        return pos_robots
    

# test
# np.array(EnvSetup().robot_initialaizer(20))
# EnvSetup().target_initializer
    