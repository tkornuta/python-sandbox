import copy

def greedy_find_path(entrance, exits, corridors):
    """ Find ANY path connecting input and output, """
    print("corridors at start: ",  corridors)
    #max_flow = float("inf")
    cur_pos = entrance
    path = []
    max_flows = []
    # Create a local copy of corridors leading to not visited rooms.
    not_visited_corridors = copy.deepcopy(corridors)
    # Find path - greedy select corridors with biggest flows.
    while (cur_pos not in exits):
        # Remove all corridors leading to visited rooms, including entrance!
        not_visited_corridors[cur_pos][entrance] = 0
        for visited in path:
            not_visited_corridors[cur_pos][visited] = 0
            
        # Find max flow in remaining corridors.
        max_flow = max(not_visited_corridors[cur_pos])
        max_flows.append(max_flow)
        # If there is no flow - break!
        if max_flow == 0:
            break
        # "Select that corridor.
        corridor = not_visited_corridors[cur_pos].index(max_flow)
        path.append(corridor)
        print ("path = ",  path)
        print ("max_flows = ",  max_flows)
        # Move! ;)
        cur_pos = corridor
    print ("path = ",  path)
    print ("max_flows = ",  max_flows)
    min_flow  = min(max_flows)
    # Check whether there  in fact is any flow!
    # Cannot do it - have to reverse "temporarily used corridors".
    #if min_flow == 0:
    #    return 0;
        
    # "Realize" flow from entrance to exit.
    print ("sending {} bunnies from {} through {}".format(min_flow,  entrance,  path))
    cur_pos = entrance
    for corridor, max_flow in zip(path,  max_flows):
         corridors[cur_pos][corridor] = corridors[cur_pos][corridor] - min_flow
         cur_pos = corridor
    print("corridors at end: ",  corridors)
    # Return number of bunnies that reached the escape pods;)
    return min_flow


def answer(entrances, exits, corridors):
    # your code here
    
    # Sum of all realised flows.
    flow_sum = 0
    for entrance in entrances:
        while 1:
            flow = greedy_find_path(entrance, exits, corridors)
            # If last flow was "empty" - we cannot move send any bunnies from this node anymore.
            if flow == 0:
                break
            flow_sum = flow_sum + flow
    return flow_sum


if __name__ == "__main__":
    
    test = 2
    
    if test == 1:
        entrances = [0]
        exits = [3]
        path = [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]
    elif test == 2:
        entrances = [0, 1]
        exits = [4, 5]
        path = [
          [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
          [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
          [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
          [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
          [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
          [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
        ]
    elif test == 3:
        entrances = [0]
        exits = [3]
        path = [[0, 7, 0, 0], [0, 0, 6, 0], [0, 8, 0, 2], [9, 0, 0, 0]]

    print(answer(entrances, exits, path)) 
    #print(answer("2",  "1001")) 
    
