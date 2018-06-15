from envSetup import EnvSetup



# pathfinder
class Pathfinder():    
    #
    def __init__(self):
        self.nodes_movable = EnvSetup().nodes_movable
            
    
    
    # 4 neighbors: east, north, west, south.
    def neighbours4(self, node):
        # 4 directions: east, north, west, south.
        dirs = [[1., 0.], [0., 1.], [-1., 0.], [0., -1.]]
        result = []
        for dir in dirs:
            neighbor = [node[0] + dir[0], node[1] + dir[1]]
            # Check for validation.
            if neighbor in self.nodes_movable:
                result.append(neighbor)
        
        return result
        
    # 8 neighbors: east, northest, north, northwest, west, southwest, south, southeast.
    def neighbours8(self, node):
        # 8 directions: east, northest, north, northwest, west, southwest, south, southeast.
        dirs = [[1., 0.], [1., 1.], [0., 1.], [-1., 1.], [-1., 0.], [-1., -1.], [0., -1.], [1., -1.]]
        result = []
        for dir in dirs:
            neighbor = [node[0] + dir[0], node[1] + dir[1]]
            # Check for validation.
            if neighbor in self.nodes_movable:
                result.append(neighbor)        
        
        return result
    
    
    
    
# test.
# node = [3, 3]
# Pathfinder().neighbours4(node)
# Pathfinder().neighbours8(node)
