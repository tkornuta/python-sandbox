def answer(panel_array):
    """ Returns the maximum product of positive and (odd) negative numbers."""
    print("panel_array=", panel_array)
    # Edge case I: no panels :]
    if (len(panel_array) == 0):
        return str(0)
        
    # Get zero panels.
    zero_panels = list(filter(lambda x: x == 0 , panel_array))
    print("zero_panels=", zero_panels)
    # Edge case II: no positive nor negative panels.
    if (len(zero_panels) == len(panel_array)):
        return str(0)

    # Get positive panels
    positive_panels = list(filter(lambda x: x >0 , panel_array))
    print("positive_panels=", positive_panels)
    positive_product = 1
    for x in positive_panels:
        positive_product *= x
    
    # Get negative panels.
    negative_panels = sorted(list(filter(lambda x: x <0 , panel_array)))
    print("negative_panels=", negative_panels)

    # Edge case III: there is only one "negative panel".
    if (len(negative_panels) == 1):
        # If this is the only panel.
        if (len(panel_array) == 1):
            return negative_panels[0]
            # If there are no positive panels, but there are some panels with zeros 
        elif (len(positive_panels) == 0) and (len(zero_panels) > 1):
            return 0
 
    # Check number of negative panels.
    if len(negative_panels) % 2 != 0: 
        # Remove smallest.
        negative_panels.pop()

    print("final negative_panels=", negative_panels)
    negative_product = 1
    for x in negative_panels:
        negative_product *= x
    
    # Return product of those two.
    return str(negative_product * positive_product)


 
if __name__ == "__main__":
    my_list = [2, -3, 1, 0, -5]
    my_list = [  -2, -3, 4,  -5]
    my_list = [-1000,  0,  -2,  2, -50,  22]
    #my_list = list(range (-51, 0))
    #my_list.append(-1)
    #my_list = buckets = [0] * 100
    #my_list = [0] * 10 + [-1000]
    print("answer: {}".format(answer(my_list)))
    
