# https://www.programcreek.com/2013/01/leetcode-spiral-matrix-java/
import numpy as np

def spiral_matrix(mat):
    
    print ("mat =\n",  mat)

    
    spiral_mat = []
    # Calculate "corners" as min
    no_corners = np.min( [int(np.ceil(mat.shape[0]/2)),  int(np.ceil(mat.shape[1]/2)) ] )
    #print(no_corners)
    
    for corner in range(no_corners):
        print ("corner = ", corner)
        # First row
        y = corner
        for x in range(corner, mat.shape[1]-corner):
            spiral_mat.append(mat[y, x]) 
        #print(spiral_mat)
        # Last column
        x = mat.shape[1]-corner-1
        for y in range(corner+1, mat.shape[0]-corner):
            spiral_mat.append(mat[y, x]) 
        print(spiral_mat)

        # If we do not have to return - corner is pointing at the column/row that was already printed "forward".
        if (corner >=  mat.shape[0]-corner-1) or (corner >=  mat.shape[1]-corner-1):
            break

        # Last row
        y = mat.shape[0]-corner-1
        for x in range(mat.shape[1]-corner-2,  corner-1, -1):
            spiral_mat.append(mat[y, x]) 
        #print(spiral_mat)
    
        # First column
        x = corner
        for y in range(mat.shape[0]-corner-2,  corner, -1):
            spiral_mat.append(mat[y, x]) 
        #print(spiral_mat)
    
    return spiral_mat
    
if __name__ == "__main__":
    # Special case I: one row
    #mat = np.matrix([ 1, 2, 3 ])
    
    # Special case II: one column
    mat = np.matrix([ [1], [2], [3] ])
    
    # Special case III: one element
    #mat = np.matrix([ 1 ])
    
    # Special case IV: no elements
    #mat = np.matrix([ ])
    
    # Special case Va: rectangle
    #mat = np.matrix([ [ 1, 2, 3, 4 ], [ 5,  7, 8, 9 ]])

    # Special case Vb: rectangle
    #mat = np.matrix([ [ 1, 2, 3 ],  [ 4, 5, 6 ], [ 7, 8, 9 ] , [ 10, 11, 12 ] ])
    
    #mat = np.matrix([ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]])
            
    print("spiral mat =\n",  spiral_matrix (mat))
