import copy

def tap(map):
    print(map)

    # Initialize left wall with elevation map.
    left_wall = copy.deepcopy(map)
    # Determine left walls.
    for i in range(1, len(left_wall)):
        if left_wall[i] < left_wall[i-1]:
            left_wall[i] = left_wall[i-1]
    print(left_wall)


    # Initialize right wall with elevation map.
    right_wall = copy.deepcopy(map)
    # Determine right walls.
    for i in range(len(right_wall)-2, -1,  -1):
        if right_wall[i] < right_wall[i+1]:
            right_wall[i] = right_wall[i+1]
    print(right_wall)

    # Calculate how many drops can fit between left and right walls.
    drops = []
    for i in range(len(map)):
        drops.append(min(left_wall[i],  right_wall[i]) - map[i])
    print(drops)
    
    return sum(drops)


if __name__ == "__main__":

    map = [0,1,0,2,1,0,1,3,2,1,2,1]
    print("Solution:")
    print(tap(map))
