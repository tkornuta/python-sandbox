# Lab126 last task
# 1. Function that adds arc to graph
# 2. Function that checks if there is a path between two nodes.
nodes = []
arcs = []

def print_graph():
    print("nodes =", nodes)
    print("arcs =", arcs)

def add_node(node1):
   # Check if nodes exist.
    if node1 not in nodes:
        nodes.append(node1)

def add_arc(node1, node2):
    # Add nodes
    add_node(node1)
    add_node(node2)
    # Check if arc exist.
    if (node1, node2) not in arcs:
        arcs.append((node1, node2))

def check_path(curr_node,  dest_node,  visited_nodes):
    # Stop condition 1: found the path!
    if curr_node == dest_node:
        return True
    # Stop condition 2: we already visited that node
    if curr_node in visited_nodes:
        return False
    
    # Add current node to visited nodes.
    visited_nodes.append(curr_node)
    
    # Check arcs from curr_node.
    for (n1, n2) in arcs:
        if (n1 == curr_node):
            if check_path(n2, dest_node,  visited_nodes):
                return True
        elif (n2 == curr_node):
            if check_path(n1, dest_node,  visited_nodes):
                return True
                
    # Sadly, we failed.
    return False
    
if __name__ == "__main__":
    # Create graph
    add_arc(1, 2)
    add_arc(1, 3)
    add_arc(3, 4)
    add_arc(5, 7)
    add_node(6)
    print_graph()

    # Check path
    print(check_path(4, 1,  []))
 
    

    
