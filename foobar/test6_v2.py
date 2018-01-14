import math

def recurseA(reqF,  reqM,  curF,  curM,  cur_depth,  best_depth):
    #print("A: reqF={},  reqM={},  curF={},  curM={},  cur_depth={},  best_depth={}".format(reqF,  reqM,  curF,  curM,  cur_depth,  best_depth))    
    # Terminal condition 1: we have found the solution. (OK)
    if (reqF == curF) and (reqM == curM):
        #print("A: OK")
        return cur_depth
        
    # Terminal condition 0: do not go deeper if we already got better solution.
    if (cur_depth > best_depth):
        return best_depth

    # Terminal condition 2: we have produced too many bombs of a given type.
    if (reqF < curF) or (reqM < curM):
        return best_depth
        
    # Ok, let's recurse!
    # Follow path B: f=f+m, m=m
    bd1 = recurseB(reqF,  reqM,  curF+curM,  curM,  cur_depth+1,  best_depth)
    if (bd1 < best_depth):
        best_depth = bd1
    
    # Follow path A: f=f, m=m+f
    bd2 = recurseA(reqF,  reqM,  curF,  curM+curF,  cur_depth+1,  best_depth)
    if (bd2 < best_depth):
        best_depth = bd2
    
    # Return best depth.
    return best_depth


def recurseB(reqF,  reqM,  curF,  curM,  cur_depth,  best_depth):
    #print("B: reqF={},  reqM={},  curF={},  curM={},  cur_depth={},  best_depth={}".format(reqF,  reqM,  curF,  curM,  cur_depth,  best_depth))
    # Terminal condition 1: we have found the solution.
    if (reqF == curF) and (reqM == curM):
        #print("B: OK")
        return cur_depth

    # Terminal condition 0: do not go deeper if we already got better solution.
    if (cur_depth > best_depth):
        return best_depth
    
    # Terminal condition 2: we have produced too many bombs of a given type.
    if (reqF < curF) or (reqM < curM):
        return best_depth
        
    # Ok, let's recurse!
    # Follow path A: f=f, m=m+f
    bd2 = recurseA(reqF,  reqM,  curF,  curM+curF,  cur_depth+1,  best_depth)
    if (bd2 < best_depth):
        best_depth = bd2
 
    # Follow path B: f=f+m, m=m
    bd1 = recurseB(reqF,  reqM,  curF+curM,  curM,  cur_depth+1,  best_depth)
    if (bd1 < best_depth):
        best_depth = bd1
 
    # Return best depth.
    return best_depth

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
    
    #best_depth = recurseA(M, F,  1,  1,  0,  float('inf'))
    #if (math.isinf(best_depth)):
    #    return "impossible"
    
    # Return sum
    #return str(best_depth)
    return reverse_problem(M, F)


if __name__ == "__main__":
    #print(answer("1",  "1")) 
    #print(answer("100000000000000000000000000000000000000000000000000",  "1")) 
    print(answer("1000000000000000000000000000000000000000000000100000",  "1000000000000000001")) 
    #print(answer("2",  "4")) # impossible
    #print(answer("4",  "7")) 

    #print(answer("1001",  "2")) 
    #print(answer("2",  "1001")) 
    
