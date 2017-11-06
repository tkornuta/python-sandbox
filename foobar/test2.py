def generous_hire(lambs):
    """  Generously pay to the henchmen."""
    # Edge case: we can pay only to the junior.
    if (lambs < 1):
        print ("Generous (special):\n [0]")
        print (" -> Sum: 0")
        return 0
    # Store payments.
    payments = []
    # Hire first Junior.
    payments.append(1)
    while (True):
        # Check the rest of sum.
        rest = lambs - sum(payments)
        # Try to "hire" new henchman, paying him "generously" twice as much.
        next = 2 * payments[-1]
        if (next > rest):
            # Edge case III: ok, we cannot pay him generously - but maybe we can still hire him!
            if (len(payments) >=2):
                next = payments[-1] + payments[-2]
                if (next <= rest):
                    # Hire!
                    payments.append(next)
            elif (len(payments) == 1):
                # We hired only the first junior!
                next = payments[-1]
                if (next <= rest):
                    # Hire!
                    payments.append(next)
                
            # Recalculate rest,
            rest = lambs - sum(payments)
            print ("Generous:\n",  payments)
            print (" -> Sum: {}".format(sum(payments)))
            print (" -> Rest: {}".format(rest))
            return len(payments)
        else:
            # Hire!
            payments.append(next)

def greedy_hire(lambs):
    """  Pay to the henchmen as low as possible"""
    # Edge case I: we can pay only to the junior.
    if (lambs < 1):
        print ("Greedy (special):\n [0]")
        print (" -> Sum: 0")
        return 0
    # Edge case II: we can pay only to the first two juniors.
    elif (lambs < 2):
        print ("Greedy (special):\n [1]")
        print (" -> Sum: 1")
        return 1
    # Store payments
    payments = []
    # Hire two juniors.
    payments.append(1)
    payments.append(1)
    while (True):
        # Check the rest of sum.
        rest = lambs - sum(payments)
        # Try to "hire" new henchman, paying him the "minimum".
        next = payments[-1] + payments[-2]
        if (next > rest):
            print ("Greedy:\n",  payments)
            print (" -> Sum: {}".format(sum(payments)))
            print (" -> Rest: {}".format(rest))
            return len(payments)
        else:
            # Hire!
            payments.append(next)

def answer(total_lambs):
    """ Returns the difference of number of henchmen paid in greedy and generously ways."""
    return greedy_hire(total_lambs) - generous_hire(total_lambs)

if __name__ == "__main__":
    while(True):
        lambs = int(input("Enter the LAMB sum:"))
        #print(generous_pay(lambs))
        print("Difference is: {}".format(answer(lambs)))
