
def reverse_problem(M,  F):
    steps = 0
    while (M > 1) and (F > 1):
        print("M = {}, F = {}, steps = {}".format(M, F, steps))
        # Greedy select fastest way down.
        if (M > F):
            # Check how many times F fits in M
            times = M // F
            M = M - F * times
        else:
            times = F // M
            F = F - M * times
        steps = steps + times
    print("after M = {}, F = {}, steps = {}".format(M, F, steps))
    if (M < 1) or (F < 1):
        #print("impossible")
        return "impossible"
    # Last steps.
    if (M > 1):
        steps = steps + M -1
    else:
        steps = steps + F -1
    print("final M = {}, F = {}, steps = {}".format(M, F, steps))
    return str(steps)

def answer(M, F):
    # your code here
    M = int(M)
    #print("M=", M)
    F = int(F)
    #print("F=", F)
    # Edge case  0: F = 1 (TEST 1)
    if (F == 1):
        print("Edge 0")
        return M-1
    # Edge case  1: M = 1
    if (M == 1):
        print("Edge 1")
        return F-1
    
    #if (M > 100000) or (F > 100000):
    #    return "max recursion depth!"

    return reverse_problem(M, F)


if __name__ == "__main__":
    #print(answer("1",  "1")) 
    #print(answer("100000000000000000000000000000000000000000000000000",  "1")) 
    #print(answer("1000000000000000000000000000000000000000000000100000",  "1000000000000000001")) 
    #print(answer("2",  "4")) # impossible
    #print(answer("4",  "7")) 

    print(answer("1001",  "2")) 
    #print(answer("2",  "1001")) 
    
