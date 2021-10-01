# From cracking, chapter 8, page 342

def rec_ways(n):
    # Recurrent solution/dynamic programming - start from the end.
    # three branches, n elements => O(3^n)
    #print("call!")
    if n < 0:
        # Edge case 0: cannot make that move - no paths.
        return 0
    elif n == 0:
        # Reached bottom - path is valid.
        return 1
    else:
        # Return all paths leading to steps leading to this one.
        #print("compute!")
        return rec_ways(n-1) + rec_ways(n-2) + rec_ways(n-3)

# Second solution - linear, with table counting
# number of paths leardin to this step.
def lin_table(n):
    #print("call")
    # O(n*3) = O(n)
    # Initialize table - with zeros.
    # First step - 0.
    # Second step - 1.
    # base, step 1, step 2, step 3, .. step n
    table = [0] * (n+1)
    # at start - a single "path leading to base".
    table[0] = 1
    for step in range(0,n):
        #print(step)
        for hop in [1,2,3]:
            # If hop is doable:
            # increment by the number of path leading to this step.
            if step + hop <= n:
                #print("compute!")
                table[step+hop] += table[step]
            #print(table)
    return table[n]

def rec_mem(n, table = None):
    #print(f"call for {n}!")
    # Recursive memorization.
    # Table: base, step 1, step 2, ..., step n.
    if table is None:
        table = [None] * (n+1)
        # One path "leads" to base.
        table[0] = 1

    if n < 0:
        # Edge case 0: cannot make that move - no paths.
        return 0
    elif table[n] is not None:
        # Reached bottom - path is valid.
        return table[n]
    else:
        #print("compute!")
        # Save number of paths leading to that step.
        table[n] = rec_mem(n-1, table) + rec_mem(n-2, table) + rec_mem(n-3, table)
        return table[n]

# For 3: 1,1,1 | 1,2 | 2,1 | 3 = 4
# For 4: 1,1,1,1 | 1,1,2 | 1,2,1 | 1, 3 | 2,1,1 | 2,2| 3,1  = 7
#print(rec_ways(28))
#print(lin_table(28))
print(rec_mem(28))


