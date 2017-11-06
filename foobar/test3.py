def calculate_abs_power(panel_array):
    """ Calculate absolute power of a given panel array"""
    non_zero_panels = list(filter(lambda x: x != 0 , panel_array))
    product = 1
    for x in non_zero_panels:
        product *= x
    return abs(product)
    

def calculate_max_power(panel_array):
    """ Returns the maximal product of positive and (odd) negative numbers."""
    # Edge case 0: no panels :]
    if (len(panel_array) == 0):
        return 0
        
    # Get positive panels
    positive_panels = list(filter(lambda x: x >0 , panel_array))
    #print("positive_panels=", positive_panels)
    positive_product = 1
    for x in positive_panels:
        positive_product *= x
    
    # Get negative panels.
    negative_panels = sorted(list(filter(lambda x: x <0 , panel_array)))

    # Edge case I: there is only one "negative panel".
    if (len(negative_panels) == 1) and (len(positive_panels) == 0):
        return negative_panels[0]
 
     # Get zero panels.
    zero_panels = sorted(list(filter(lambda x: x == 0 , panel_array)))
    # Edge case II: no positive panels.
    if (len(zero_panels) == len(panel_array)):
        return 0

    # Check number of negative panels.
    if len(negative_panels) % 2 != 0: 
        # Remove smallest.
        negative_panels.pop()

    #print("negative_panels=", negative_panels)
    negative_product = 1
    for x in negative_panels:
        negative_product *= x
    
 
    # Return product of those two.
    return negative_product * positive_product

def answer(all_panels):
    # Single, considered array of panel.
    panel_array =[]
    # List containing powers of arrays of panels.
    panel_arrays_powers =[]

    # Iterate through all panels.
    while len(all_panels) > 0:
        # Take first element and add it to the list.
        panel_array.append(all_panels.pop(0))
        abs_power = calculate_abs_power(panel_array)
        # Check whether we did not exceeded max absolute power nor max number of panels.
        if (abs_power >1000) or (len(panel_array) >= 50):
            # Remove last panel and recalculate power.
            last_panel = panel_array.pop()
            power = calculate_max_power(panel_array)
            print("panel_array {} with max power {}".format(panel_array, power))
            # Add panel power to list.
            panel_arrays_powers.append(power)
            # Start new panel array: clear the list and add last panel to it.
            panel_array = [last_panel]
    
    # Handle last ("unfinished") panel array.
    power = calculate_max_power(panel_array)
    print("last panel_array {} with max power {}".format(panel_array, power))
    panel_arrays_powers.append(power)

    # Return the resuls - as string.
    s = ""
    for x in panel_arrays_powers:
        s += str(x) + ","
    # Remove last comma
    s = s[:-1]
    return s

 
if __name__ == "__main__":
    my_list = [2, -3, 1, 0, -5]
    my_list = [  -2, -3, 4,  -5]
    my_list = [-1000,  0,  -2,  2, -50,  22]
    #my_list = list(range (-51, 0))
    #my_list = buckets = [0] * 100
    print("answer: {}".format(answer(my_list)))
    
