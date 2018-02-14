import math

def inplace_rotate_square_matrix(mat):
    # Iterate through "squares".
    for s in range(math.floor(len(mat)/2)):
        # Iterate through elements lying on a given square side.
        #s = 1
        for x in range(len(mat)-1-2*s):
        #for x in range(1):
            #x = 2
            tmp = mat[s][s+x]
            # Replace respective elements on four sides of the square.
            mat[s][s+x] = mat[s+x][-1-s]
            mat[s+x][-1-s] = mat[-1-s][-1-s-x]
            mat[-1-s][-1-s-x] = mat[-1-s-x][s]
            mat[-1-s-x][s] = tmp

    return mat

if __name__ == "__main__":
    
    #mat =  [[1 ,  2 ,  3],  [4,   5,   6],  [7, 8, 9]]
    #mat =  [[1, 2, 3, 4],  [5, 6, 7, 8],  [9, 10, 11, 12], [13, 14, 15, 16]]
    mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

    print (inplace_rotate_square_matrix(mat))
