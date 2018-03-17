# https://www.programcreek.com/2014/05/leetcode-minimum-path-sum-java/
# but not really :] Those are the solutions for a general problem of finding the minimum path in a graph.
import numpy as np



def generate_path(map,  dist, sy,  sx,  dy,  dx):
    ''' Generates (and visualizes) path from (sy,sx) to (dy,dx)'''
    # We got the distance map, not build the path by simply picking the nodes with smallest cost.
    path = [['.' for x in range(map.shape[1])] for y in range(map.shape[0])]
    
    # "Initialize" position.
    x = sx
    y = sy
    
    while y != dy or x != dx:
        next_x = -1
        next_y = -1
        next_min = np.inf
        move = 'x'
        # Check four directions.
        if (x > 0)  and (dist[y,  x-1] < next_min):
            next_min = dist[y,  x-1]
            next_x = x-1
            next_y = y
            move = '<'
        if (x < map.shape[1]-1)  and (dist[y,  x+1] < next_min):
            next_min = dist[y,  x+1]
            next_x = x+1
            next_y = y
            move = '>'
        if (y > 0)  and (dist[y-1,x] < next_min):
            next_min = dist[y-1, x]
            next_x = x
            next_y = y-1
            move = '^'
        if (y < map.shape[0]-1)  and (dist[y+1,x] < next_min):
            next_min = dist[y+1,x]
            next_x = x
            next_y = y+1
            move = 'd'
        # Make move
        path[y][x] = move
        x = next_x
        y = next_y
    
    # Indicate start and destination nodes.
    path[sy][sx] = 'o'
    path[dy][dx] = 'x'
    return path

def recursive_cost(map,  dist,  y, x):
    if (x > 0) and (dist[y, x-1] > dist[y, x] + map[y, x]):
        dist[y, x-1] = dist[y, x] + map[y, x-1]
        recursive_cost(map,  dist,  y, x-1)

    if (x < map.shape[1]-1) and (dist[y, x+1] > dist[y, x] + map[y, x+1]):
        dist[y, x+1] = dist[y, x] + map[y, x+1]            
        recursive_cost(map,  dist,  y, x+1)
        
    if (y > 0) and (dist[y-1, x] > dist[y, x] + map[y-1, x]):
        dist[y-1, x] = dist[y, x] + map[y-1, x]
        recursive_cost(map,  dist,  y-1, x)

    if (y < map.shape[0]-1) and (dist[y+1, x] > dist[y, x] + map[y+1, x]):
        dist[y+1, x] = dist[y, x] + map[y+1, x]            
        recursive_cost(map,  dist,  y+1, x)
    # return 


def min_path_recursive(map, start=None,  dest=None):
    '''Finds minimum path in a given map using a simple recursive algorithm'''
    print(map.shape)
    print("Map:\n",map)    

    # Initialize cost map.
    dist = np.empty(map.shape)
    dist.fill(np.inf)
    
    # Get start and destination coordinates.
    if (start == None):
        sy=0
        sx=0
    else:
        sy=start[0]
        sx=start[1]    
    if (dest == None):
        dy = map.shape[0]-1
        dx = map.shape[1]-1
    else:
        dy = dest[0]
        dx = dest[1]

    # Distance from dest to dest is set to 0
    dist[dy, dx] = 0
    
    recursive_cost(map,  dist,  dy, dx)
    
    print("Final distances:\n", dist)

    return generate_path(map,  dist,   sy,  sx,  dy,  dx)


def min_path_dijkstra(map, start=None,  dest=None):
    '''Finds minimum path in a given map using the Dijkstra algorithm'''
    print(map.shape)
    print("Map:\n",map)    
    
    # Initialize cost map.
    dist = np.empty(map.shape)
    dist.fill(np.inf)

    # Get start and destination coordinates.
    if (start == None):
        sy=0
        sx=0
    else:
        sy=start[0]
        sx=start[1]    
    if (dest == None):
        dy = map.shape[0]-1
        dx = map.shape[1]-1
    else:
        dy = dest[0]
        dx = dest[1]

    # Distance from dest to dest is set to 0
    dist[dy, dx] = 0
    
    #  Queue of all nodes in the graph.
    Q  = [(y, x) for y in range(map.shape[0]) for x in range(map.shape[1])]
 
    while any(Q):
        #print("Q=", Q)
        # Find node with minimum distance to target.
        min_dist = np.inf
        min_node =-1
        for i, (y, x) in enumerate(Q):
            if (dist[y, x] < min_dist):
                min_dist = dist[y, x] 
                min_node = i
        # Propagate from that node...
        (y, x) = Q.pop(min_node)

        # ... for each new adjacent node - check distances.
        if (x > 0) and (dist[y, x-1] > dist[y, x] + map[y, x]):
            dist[y, x-1] = dist[y, x] + map[y, x-1]

        if (x < map.shape[1]-1) and (dist[y, x+1] > dist[y, x] + map[y, x+1]):
            dist[y, x+1] = dist[y, x] + map[y, x+1]            
            
        if (y > 0) and (dist[y-1, x] > dist[y, x] + map[y-1, x]):
            dist[y-1, x] = dist[y, x] + map[y-1, x]

        if (y < map.shape[0]-1) and (dist[y+1, x] > dist[y, x] + map[y+1, x]):
            dist[y+1, x] = dist[y, x] + map[y+1, x]            

        #print("Calculated distances:\n", dist)
    print("Final distances:\n", dist)

    # Path.
    if (start == None):
        sy=0
        sx=0
    else:
        sy=start[0]
        sx=start[1]
        
    return generate_path(map,  dist,   sy,  sx,  dy,  dx)
    
if __name__ == "__main__":
    #map = np.array([[1, 2, 11, 10],   [2, 1, 1, 1],  [2, 1, 4, 0]])
    #map = np.array([[1, 30, 1, 3,  1],   [2, 1, 1, 10,  1],  [2, 1, 40, 1,  1]])
    map = np.array([[1, 2, 111, 10],   [21, 1, 101, 11],  [2, 1, 40, 9],  [1, 10, 40, 9],  [1, 1, 10, 1]])

    #p = min_path_dijkstra(map,  start=(0, 0),  dest=(0, 3))
    p = min_path_recursive(map=map,  start=(0, 0),  dest=(2, 3))
    print("Final path: ")
    for row in p:
        print(row) 
