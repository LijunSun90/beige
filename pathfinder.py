from envSetup import EnvSetup
import collections
import heapq
    

# queue
class Queue:
    def __init__(self):
        self.elements = collections.deque()
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, x):
        self.elements.append(x)
    
    def get(self):
        return self.elements.popleft()

    
    
#    
class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

    

# pathfinder
class Pathfinder():    
    #
    def __init__(self):
        self.nodes_passable = EnvSetup().nodes_passable
        self.nodes_all = EnvSetup().nodes_all
        self.nodes_obstacleStatic = EnvSetup().nodes_obstacleStatic
        self.nodes_obstacleDynamic = EnvSetup().nodes_obstacleDynamic
        
        self.nodes_start = EnvSetup().nodes_target_initializer[0]
        self.nodes_goals = EnvSetup().nodes_robot_initializer
        self.came_from = {}
        self.cost_so_far = {}
            
    
    # Check if the node is passalbe.
    def passable(self, node):
        if node in (set(self.nodes_all) - set(self.nodes_obstacleStatic)):
            return True
        else:
            return False

        
    
    # Check if the node is passable in the diagonal direction.
    def passableDiagonal(self, from_node, to_node):
        node_diagonal_block_1 = (to_node[0], from_node[1])
        node_diagonal_block_2 = (from_node[0], to_node[1])
        if node_diagonal_block_1 in self.nodes_obstacleStatic or node_diagonal_block_2 in self.nodes_obstacleStatic:
            return False
        else:
            return True
        
        
    
    # 4 neighbors: east, north, west, south.
    def neighbors4(self, node):
        # 4 directions: east, north, west, south.
        dirs = [(1., 0.), (0., 1.), (-1., 0.), (0., -1.)]
        result = []
        for dir in dirs:
            neighbor = (node[0] + dir[0], node[1] + dir[1])
            # Check for validation.
            if self.passable(neighbor):
                result.append(neighbor)
        
        return result
    
    
    # 8 neighbors: east, northest, north, northwest, west, southwest, south, southeast.
    def neighbors8(self, node):
        # 8 directions: east, northest, north, northwest, west, southwest, south, southeast.
        dirs = [(1., 0.), (1., 1.), (0., 1.), (-1., 1.), (-1., 0.), (-1., -1.), (0., -1.), (1., -1.)]
        result = []
        for dir in dirs:
            neighbor = (node[0] + dir[0], node[1] + dir[1])
            # Check for validation.
            if self.passable(neighbor) and self.passableDiagonal(node, neighbor):
                result.append(neighbor)        
        
        return result
    
    
    # Define the cost function.
    def cost(self, from_node, to_node):
        return 1 
    
    
    # Define the heuristic function.
    def heuristic(self, node, goal):
        dx = abs(node[0] - goal[0])
        dy = abs(node[1] - goal[1])
        # D: the cost of moving horizontally or vertically.
        # D2: the cost of moving diagonally.
        # Chebyshev distance: D = 1 and D2 = 1. 
        # Octile distance: When D = 1 and D2 = sqrt(2).
        D = 1
        D2 = 1
        return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)
    

    # Build the path.
    def reconstruct_path(self, goal):
        path = []
        current = goal
#         print("start:", self.nodes_start)
#         print("goal:", goal)
#         print("current:", current)
        while current != self.nodes_start:
            path.append(current)
            current = self.came_from[current]
        path.append(self.nodes_start) # optional
        path.reverse() # optional
        return path
    
    
    # A*
    def a_star_search(self):
        #
        frontier = PriorityQueue()
        frontier.put(self.nodes_start, 0)
        #
        self.came_from.clear()
        cost_so_far = {}
        self.came_from[self.nodes_start] = None
        cost_so_far[self.nodes_start] = 0
        #
        while not frontier.empty():
            current = frontier.get()
            
            # Early exit.
            if current == goal:
                break

            for next in self.neighbors8(current):
                new_cost = cost_so_far[current] + self.cost(current, next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + heuristic(next, goal)
                    frontier.put(next, priority)
                    self.came_from[next] = current
            
            
    # breadth_first_search
    def breadth_first_search(self):
        frontier = Queue()
        frontier.put(self.nodes_start)
        self.came_from.clear()
        self.came_from[self.nodes_start] = None
        self.cost_so_far.clear()
        self.cost_so_far[self.nodes_start] = 0
        goals = self.nodes_goals.copy()

        count = 0
        while not frontier.empty():
            current = frontier.get()
            
            # Early exit.
            if current in goals:
                print("Reach the goal", count, ":", current)
                count = count + 1
                goals.remove(current)
            if len(goals) == 0:
                break
            
            neighbors = self.neighbors8(current)
            for next in neighbors:
                new_cost = self.cost_so_far[current] + self.cost(current, next)
                if next not in self.came_from:
                    frontier.put(next)
                    self.came_from[next] = current
                    self.cost_so_far[next] = new_cost
        
        return self.came_from
    
    


    
# test.
# node = [3, 3]
# Pathfinder().neighbours4(node)
# Pathfinder().neighbours8(node)
# pathfinder = Pathfinder()
# pathfinder.breadth_first_search()
# pathfinder.reconstruct_path(pathfinder.nodes_goals[0])