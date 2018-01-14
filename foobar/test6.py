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

def answer(M, F):
    # your code here

    
    M = int(M)
    print("M=", M)
    F = int(F)
    print("F=", F)
    # Edge case  0: F = 1 - TEST 1
    if (F == 1):
        print("Edge 0")
        return M-1
    # Edge case  1: M = 1
    if (M == 1):
        print("Edge 1")
        return F-1
    
    if (M > 100000) or (F > 100000):
        return "impossible"
    
    best_depth = recurseA(M, F,  1,  1,  0,  float('inf'))
    
    if (math.isinf(best_depth)):
        return "impossible"
    
    # Return sum
    return str(best_depth)


if __name__ == "__main__":

    #print(answer("1",  "1")) 
    #print(answer("100000000000000000000000000000000000000000000000000",  "1")) 
    print(answer("2",  "4")) 
    
    #print(answer("4",  "7")) 

    #print(answer("1000",  "1")) 

