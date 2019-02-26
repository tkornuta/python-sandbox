// Find all constructable
//
// Now, I’ll give you a list of all possible hypotenuses of the 
// right triangle and a list of all desired areas of the triangle.
//
// I want to know how many combinations of hypotenuses and areas 
// are valid.
//
// Example:
// Input:  H = [1, 6, 4, 3], A = [35, 3, 99, 5]
// { (h,a) for all h in H for all a in A } -> filter valid combinations
// Output: 3
//         Valid combinations are:
//           (h, a) = (6, 3) # (H[1], A[1])
//           (h, a) = (6, 5) # (H[1], A[3])
//           (h, a) = (4, 3) # (H[2], A[1])
// +
// |\
// | \ h
// |a \
// +---+



#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;


int main() {
  vector<int> h = {1, 6, 4, 3};
  // vector<int> a = {35, 3, 99, 5};
  vector<int> a = {3,5};
  //vector<int> h = {1, 3, 4, 6};
  //vector<int> a = {3, 5, 35, 99};

  // Sort both lists.
  std::sort(h.begin(), h.end());
  std::sort(a.begin(), a.end());
  

  int all_valid_combinations =0;
  
  size_t hi=0, ai=0;
  while((hi < h.size()) and (ai < a.size())) {
    // Calculate the max area.
    int max_area = h[hi]*h[hi];
    int area = a[ai];
    // Compare the areas.
    if (max_area >= 4*area) {
        ai++;
        // I
        if (ai == a.size()) {
          all_valid_combinations += a.size() * (h.size() - hi);
        }
    } else {
      hi++;
      all_valid_combinations += ai;
    }//: else
    
  }//: while
    
  cout << all_valid_combinations << endl;


	return 0;
}//: main


/*int main2() {
  vector<int> h = {1, 6, 4, 3};
  vector<int> a = {35, 3, 99, 5};


  int all_valid_combinations =0;
  
  for(size_t i=0; i<h.size(); i++) {
    // Calcualte the max area.
    int max_area = h[i]*h[i];

    for(auto area: a) {
      // Compare the max area.
      if (4*area <= max_area)
        all_valid_combinations++;
    }//: for
    
  }
  cout << all_valid_combinations << endl;


	return 0;
}*/