# Count the number of raindrops falling on a stretch of pavement. Given a fixed list of drops, count how many are required to wet the entire stretch. 
# Given: pavement_start_pos, pavement_end_pos, drops=[drop_0_start, drop_0_end, drop_1_start, ...]
# Return: int

# Example: 0.0, 1000.0, [(5.0, 67.8), (-10, 10.2), (66.78, 66.79), (4.0, 1001.0), (6.7, 7.8)]
# Expects: 4

# Start, end, [(start_1, end_1), ...]

def accumulate_puddles(coverage, drop):
    # Edge case: no coverage.
    if len(coverage) == 0:
        coverage.append(drop)
        return
    # Other cases: extend.
    #import pdb; pdb.set_trace()
    # Try to find overlap.
    for puddle in coverage:
        # Full overlap (drop inside of a puddle): nothing changes.
        if puddle[0] <= drop[0] and puddle[1] >= drop[1]:
            return
        # No overlap (with that particular puddle!)
        elif drop[1] < puddle[0] or drop[0] > puddle[1]:
            coverage.append(drop)
            continue
        # Remaining cases: left and right overlap.
        extended = False
        
        # First: left overlap - don't care about right!
        if drop[0] < puddle[0] and drop[1] >= puddle[0]:
            # Extend to the left.
            puddle[0] = drop[0]
            # Remove that puddle and add new, extended one.
            extended = True
        # Second: right overlap - don't care about left!
        if drop[0] <= puddle[1] and drop[1] > puddle[1]:
            # Extend to the right.
            puddle[1] = drop[1]
            # Remove that puddle and add new, extended one.
            extended = True
        # Check if we can break the loop.
        if extended:
            return    

def check_coverage(start_pos, end_pos, coverage):
    """ Check whether the entire stretch is covered."""
    for puddle in coverage:
        if puddle[0] <= start_pos and puddle[1] >= end_pos:
            return True
    return False

def count_drops(start_pos, end_pos, drops):
    """" Returns the index of the last drop required to cover the entire stretch. """
    # List of puddles - regions covered with water.
    coverage = []
    # Number of required drops.
    num_of_drops = 0
    
    for drop in drops:
        # Increment the drop.
        num_of_drops += 1
        #print(num_of_drops, ": ", drop)
        
        # Add drop and change it to a list.
        accumulate_puddles(coverage, [drop[0], drop[1]])
        #print(coverage)
        
        if check_coverage(start_pos, end_pos, coverage):
            return num_of_drops
        
    # Ok, we still haven't covered the whole stretch.
    return "Not enough raindrops!"


print('expect 1, got', count_drops(0.0, 1000.0, [(-1.0, 1001.0), (0.0, 1000.0)]))
print('expect 4, got', count_drops(0.0, 1000.0, [(5.0, 67.8), (-10, 10.2), (66.78, 66.79), (4.0, 1001.0), (6.7, 7.8)]))
print('expect 3, got', count_drops(0.0, 1000.0, [(1.0, 2.0), (4.0, 5.0), (0.0, 1000.0), (50.0, 60.0), (0.0, 1000.0)]))

# Outside of the range - still counts ;)
# Pavement is dry at the start ;)
# Right is always > left.