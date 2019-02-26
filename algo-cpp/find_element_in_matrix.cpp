#include <iostream>
#include <vector>
using namespace std;

  bool exists(vector< vector<int > > matrix, int el ){
    /*
      *   0 4 8
      *   2 6 9
      *   2 7 10
      */
    // Get matrix size.
    size_t height = matrix.size();
    // Assume: height > 0.
    size_t width = matrix[0].size();

    /*
    // Brute force solution.
    for (size_t y=0; y<height; y++)
      for (size_t x=0; x<height; x++)
        if (matrix[y][x] == el)
          return true;
    return false;
    */

    // Idea: start from bottom left corner!
    int xp =0, yp=height-1;
    while((yp >=0 ) and (xp < width)) {
        cout << yp << "," << xp << endl;
        // Check if we found the element.
        if (matrix[yp][xp] == el)
          return true;

        if (matrix[yp][xp] > el)
            yp--;
        else
            xp++;   
    }//: while

    return false;
  }



int main() {
    vector< vector<int > > matrix;
    //vector<int> a({0 4 8});
    matrix.push_back(vector<int>({0, 4, 8}));
    matrix.push_back(vector<int>({2, 6, 9}));
    matrix.push_back(vector<int>({2, 7, 10}));

    if (exists(matrix, 5))
	    cout<<"Exists!\n";
    else
	    cout<<"Not Exists!\n";
	return 0;
}
