import copy

def greedy_find_path(entrance, exits, corridors):
    """ Find ANY path connecting input and output, """
    print("corridors at start: ",  corridors)
    #max_flow = float("inf")

    # Not the case.
    #if entrance in exits:
    #    return 1/0
        
    cur_pos = entrance
    path = [entrance]
    max_flows = [2000000]
    # Create a local copy of corridors leading to not visited rooms.
    not_visited_corridors = copy.deepcopy(corridors)
    # Find path - greedy select corridors with biggest flows.
    while (cur_pos not in exits):
        # Remove all corridors leading to visited rooms, including entrance and "recurrent corridors"!
        not_visited_corridors[cur_pos][entrance] = 0
        not_visited_corridors[cur_pos][cur_pos] = 0 # recurrent
        #for visited in path:
        #    not_visited_corridors[cur_pos][visited] = 0
        print("not_visited_corridors: ",  not_visited_corridors)
            
        # Find max flow in remaining corridors.
        max_flow = max(not_visited_corridors[cur_pos])
        corridor = not_visited_corridors[cur_pos].index(max_flow)
        print ("found corridor {} with flow {}".format(corridor,  max_flow))
        # Reset that path.
        not_visited_corridors[cur_pos][corridor] = 0
        # If there is no flow - move back!
        if max_flow == 0:
            # Move back.
            path.pop()
            max_flows.pop()
            # if we came back to entrance - there is no other path.
            if not path:
                return 0
            cur_pos = path[-1]
            print ("moving back to ",  cur_pos)
            continue
        # "Select that corridor.
        max_flows.append(max_flow)
        path.append(corridor)
        print ("selecting corridor {} with flow {}".format(corridor,  max_flow))
        print ("path = ",  path)
        print ("max_flows = ",  max_flows)
        # Move! ;)
        cur_pos = corridor
    print ("whole path = ",  path)
    print ("whole max_flows = ",  max_flows)
    min_flow  = min(max_flows)
    # Check whether there  in fact is any flow!
    if min_flow == 0:
        return 0;
        
    # "Realize" flow from entrance to exit - in original corridors!
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
 
    # Not the case.
    #if not entrances:
    #    return 1/0

    # Not the case.
    #if not exits:
    #    return 1/0
 
    # Not the case.
    # Limit all flows to 2000000.
    #for i in range(len(corridors)):
    #    for j in range(len(corridors)):
    #        if corridors[i][j] > 2000000:
    #            return 1/0
    
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
    elif test == 4:
        entrances = [0]
        exits = [3]
        path = [[9, 2, 7, 0], [0, 120, 0, 60], [0, 0, 2, 0], [9, 0, 0, 0]]
    elif test == 5:
        entrances = [0, 1]
        exits = [3]
        path = [[0, 20, 7, 0], [0, 0, 120, 20], [0, 0, 2, 0], [9, 0, 0, 0]]

    print(answer(entrances, exits, path)) 
    #print(answer("2",  "1001")) 
    
