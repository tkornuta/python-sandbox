#import copy
from fractions import Fraction,  gcd


def format_state_probabilities(terminal_states,  terminal_state_probabilities):
    """ Function changes the normalized state probabilities into format numerators-denominator """

    # Remove states that are not terminal.
    filtered_state_probabilities = []
    for i in range(len(terminal_states)):
        if (terminal_states[i]):
           filtered_state_probabilities.append(terminal_state_probabilities[i])
     
    # Remove only the initial_state.
    #filtered_state_probabilities = terminal_state_probabilities
    #print("filtered_state_probabilities before pop:",  filtered_state_probabilities)
    #filtered_state_probabilities.pop(0)
    #print("filtered_state_probabilities after pop:",  filtered_state_probabilities)

    # Special case  0: no states!
    if (len(filtered_state_probabilities) == 0):
        #print("There are no final states!")
        return []

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
    
    
# Additional limits:
# 1: The probability of reaching terminal is almost 0.
EPS = 1e-3
# 2: We've made to many steps.
MAX_DEPTH = 1e1

def recursive_transform(trans_probs,  terminal_states,  terminal_state_probabilities,  current_row,  current_path,  current_path_conditional_probability):
    print("I'm in {}, travelled the path ({}): {}".format(current_row,  current_path_conditional_probability,  current_path))
    # Stop condition I: terminal state - found a path!
    if (terminal_states[current_row]):
        # Update 
        print("Reached terminal state {} (path probability: {}) with path: {}".format(current_row,  current_path_conditional_probability,  current_path))
        terminal_state_probabilities[current_row] += current_path_conditional_probability
        return terminal_state_probabilities  
    
    # Stop condition II: going deeper makes no sense as conditional probability of given path is extremelly small.
    if (current_path_conditional_probability < EPS) or (len(current_path) > MAX_DEPTH):
        print("Cannot reach terminal state {} (path probability: {}) with path: {}".format(current_row,  current_path_conditional_probability,  current_path))
        # No change in terminal states.
        return terminal_state_probabilities
    
    for i in range(len(trans_probs[current_row])):
        # Skip transition from given state to the same state.
        if (i == current_row):
            continue
        # Skip transitions with 0 probability.
        if (trans_probs[current_row][i] == 0):
            continue
        # Else: ok, lets follow that path further.
        #next_path = copy.deepcopy(current_path)
        next_path = [el for el in current_path]
        next_path.append(i)
        # Calculate path probability - substracting EPS in odred to avoid the infinite loops.
        next_path_cond_prob = current_path_conditional_probability * trans_probs[current_row][i]
        terminal_state_probabilities = recursive_transform(trans_probs,  terminal_states,  terminal_state_probabilities,  i,  next_path,  next_path_cond_prob)
    # If we reached here means that we have checked all paths leading from given row to the end.
    return terminal_state_probabilities
    
    
def answer(m):
    """ Calculates the probabilities of reaching the terminal states"""

    # Edge case 0: empty matrix.
    if (len(m) == 0):
        #print("Matrix m is empty")
        return []
        
    # Edge case 1: badly formed matrix?
    no_states = len(m)
    #for i in range(no_states):
    #    if (len(m[i]) != no_states):
    #        print("Matrix m is not square (length of row {} is {} != {})".format(i,  len(m[i]),  no_states))
    #        return []
    
    # Preprocessing - set self-transitions to 0
    
    # Calculate tmp variable - sums of rows
    row_sums = [sum(i)  for i in m]
    #print("row_sums=", row_sums)
    # Calculate transition probabilities
    trans_probs = []
    for i in range(no_states):
        if (row_sums[i] != 0):
            trans_probs.append( [j/row_sums[i] for j in m[i]])
        else:
            # All zeros! In that case let's assume that the ore will stay in that state
            # Add transition i=>i  with prob = 1 ?
            trans_probs.append(m[i])
    print("trans_probs=", trans_probs)
    return

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

    print("terminal_states=", terminal_states)
    
    # Edge case 1: no terminal states.
    #if (sum([int(i) for i in terminal_states]) == 0):
    #    #print("No terminal nodes!")
    #    return []
            

    # Start with row zero and initial probabilities.
    # Reset terminal state probabilities.
    terminal_state_probabilities = [0 for i in row_sums]
    
    # Edge case 2: there is no exit from the 0th state - it's terminal.
    if (row_sums[0] == 0):
        print("0-th node is terminal!")
        terminal_state_probabilities[0] = 1
        return format_state_probabilities(terminal_states,  terminal_state_probabilities)
    
    for i in range(len(trans_probs[0])):
        # Skip transition from state 0 to state 0.
        if (i == 0):
            continue
        # Skip transitions with 0 probability.
        if (trans_probs[0][i] == 0):
            continue
        # Else: ok, lets follow that path further.
        current_path = [0,  i]
        terminal_state_probabilities = recursive_transform(trans_probs,  terminal_states,  terminal_state_probabilities,  i,  current_path,  trans_probs[0][i])
    # Ok, got the probabilities, now find numerators and  denominator.
    #print("terminal_state_probabilities=", terminal_state_probabilities)
   
    # Return formated probabilities
    return format_state_probabilities(terminal_states,  terminal_state_probabilities)


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
    ore_trans_mat = [[0,1,0,1], [1, 0, 0, 1], [0, 0, 0, 0], [0, 1, 1, 0]]
    

    print(answer(ore_trans_mat))
    

