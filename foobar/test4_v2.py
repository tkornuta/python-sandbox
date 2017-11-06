from fractions import Fraction,  gcd


def format_state_probabilities(terminal_states,  terminal_state_probabilities):
    """ Function changes the normalized state probabilities into format numerators-denominator """

    # Remove states that are not terminal.
    filtered_state_probabilities = []
    for i in range(len(terminal_states)):
        if (terminal_states[i]):
           filtered_state_probabilities.append(terminal_state_probabilities[i])

    # Special case  0: no states!
    if (len(filtered_state_probabilities) == 0):
        #print("There are no final states!")
        return [1]

    numerators = []
    denominators = []
    fractions = [ Fraction(prob).limit_denominator() for prob in filtered_state_probabilities]
    #print("Fractions: {}".format(fractions))
    
    # Handle separatelly numerators and denominators.
    for frac in fractions:
        numerators.append(frac.numerator)
        denominators.append(frac.denominator)
    #print("numerators: {}".format(numerators))
    #print("denominators: {}".format(denominators))
    
    denominator_changed = True
    while(denominator_changed):
        # Let's assume that everything is ok.
        denominator_changed = False
        # For every pair of fractions.
        for i in range(len(fractions)):
            # Skip zeros.
            if (numerators[i] == 0):
                continue
            for j in range(len(fractions)):
                if (i == j):
                    continue
                # Skip zeros.
                #if (numerators[j] == 0):
                #    continue
                #print("Comparing {}/{} with {}/{}".format(numerators[i], denominators[i],  numerators[j],   denominators[j]))
                # Skip equal denominators.
                if (denominators[i] == denominators[j]):
                    continue
                else:
                    # Otherwise: get greatest common denominator.
                    tmp = gcd(fractions[i], fractions[j])
                    if (denominators[i] > denominators[j]):
                        frac = tmp.denominator // denominators[j]
                        #print("frac j=", frac)
                        denominators[j] = denominators[j] * frac
                        numerators[j] = numerators[j]  * frac
                    else:
                        frac = tmp.denominator // denominators[i]
                        #print("frac i=", frac)
                        denominators[i] = denominators[i] * frac
                        numerators[i] = numerators[i] * frac
                # Note that we changed one of the denominators
                denominator_changed = True
                #print("numerators: {}".format(numerators))
                #print("denominators: {}".format(denominators))
                        
    # Sanity check
    #if (sum(numerators) != denominators[0] ):
        #print("Error! Numerators do not sum to denominator!")

    # Format output
    #output = copy.deepcopy(numerators)
    output = [int(el) for el in numerators]
    output.append(int(denominators[0]))
    return output
  


# Maximum number of considered transitions.
MAX_STEPS = 200
    
def answer(m):
    """ Calculates the probabilities of reaching the terminal states"""

    # Edge case 0: empty matrix.
    if (len(m) == 0):
        print("Input matrix is empty")
        return []
        
    # Edge case 2: 1d matrix.
    if (len(m) == 1):
        print("Input matrix is 1d")
        return [1, 1]

    # Edge case 2: badly formed matrix?
    no_states = len(m)
    #for i in range(no_states):
    #    if (len(m[i]) != no_states):
    #        print("Input matrix is not square (length of row {} is {} != {})".format(i,  len(m[i]),  no_states))
    #        return []
    
    # Calculate tmp variable - sums of rows
    row_sums = [sum(i)  for i in m]
    #print("row_sums=", row_sums)
 
    # Get terminal states
    terminal_states = []
    for i in range(no_states):
        # If there are no outputs.
        if (row_sums[i] == 0):
            terminal_states.append(True)
        # Or all outputs lead to the same node (diagonal):
        elif (len(m[i]) >i) and (row_sums[i] == m[i][i]) :
            terminal_states.append(True)
        else:
            terminal_states.append(False)
 
    # Form the Markov transition matrix.
    transition_matrix = []
    for i in range(no_states):
        if (row_sums[i] != 0):
            transition_matrix.append( [j/row_sums[i] for j in m[i]])
        else:
            # All zeros! In that case let's assume that the ore will stay in that state
            # Add self-transitions for terminal nodes: i=>i  with prob = 1
            transition_matrix.append(m[i])
            transition_matrix[i][i] =1
    print("transition_matrix=", transition_matrix)

    # Initial state.
    prev_ore_state = transition_matrix[0]
    print("initial_ore_state=", prev_ore_state)

    # Lets "evolve" the ore, starting from the first state, using PageRank.
    for i in range(MAX_STEPS):
        ore_state = []
        # Get columns from 
        for col in zip(*transition_matrix):
            # Sum all probabilities leading to a given state
            ore_state.append(sum([a*b for a,b in zip(prev_ore_state,  col)]))
            #print(zip(prev_state) * col)
        prev_ore_state = ore_state
    
    print("final_ore_state=", ore_state)

    # Return formated probabilities
    return format_state_probabilities(terminal_states,  ore_state)


if __name__ == "__main__":
    ore_trans_mat = [
      [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
      [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
      [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
      [0,0,0,0,0,0],  # s3 is terminalnumerators
      [0,0,0,0,0,0],  # s4 is terminal 
      [0,0,0,0,0,0],  # s5 is terminal
    ]
    
    #ore_trans_mat =   [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    #ore_trans_mat = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    
    # Tricky cases!
    #ore_trans_mat =   [[], []]

    #ore_trans_mat =   [[0, 1,  0], [0, 1,  0],  [0, 1, 0]]

    #ore_trans_mat =   [[0,  2,  3,  4]]
    
    #ore_trans_mat =   [[0, 2], [1],  [0], [0, 0]]
    
    #ore_trans_mat =   [[1]]
    #ore_trans_mat =   [[0,  0],  [0, 1]]
    #ore_trans_mat = [[0,1,0,1], [1, 0, 0, 1], [0, 0, 0, 0], [0, 1, 1, 0]]
    
    #ore_trans_mat

    print(answer(ore_trans_mat))
    

