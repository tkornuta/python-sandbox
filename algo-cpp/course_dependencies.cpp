#include <iostream>
#include <vector>
using namespace std;


std::vector<int> nodes;
std::vector<std:pair <int , int> > edges;

/// Inserts a single node into graph
bool insert_node(int n){
  // If node exists.
  std::vector<int>::iterator it = find(nodes.begin(), nodes.end(), n);
  if (it == nodes.end())
    return true;
  // Ok, add that node.
  nodes.push_back(n);
}

// Inserts an edge.
bool insert_edge(int module, int dependency) {
  // Try to add both nodes.
  insert_node(module);
  insert_node(dependency);
  // Add the "link" between those two.
  // TODO: Check whether link already exists.
  edges.push_back(make_pair(module, dependency));
  return true;
}


bool recursive_explore(int n, std::vector<int> to_visit, std::vector<int> visited, std::vector<int> path){
    return true;    
}



bool start_exploring(){
  // Structures used during graph traverse.
  std::vector<int> visited;
  // I need to visit all nodes.
  std::vector<int> to_visit;
  for (int n: nodes) {
    to_visit.push_back(n);
  }
  // This is "path".
  std::vector<int> path;
  for (int n: nodes) {
    // Current node.
    if recursive_explore(n, to_visit, visited, path){
      // Ok, I visited all the nodes.
      for (int np: path){
        cout << np << " < ";
      }//: for path
      cout << endl;
      // That's all folks.
      return true;
    }//: if 
  }//: for all nodes
  return false;
}


int main() {
	cout<<"Hello";
	return 0;
}

// Input:
// (dependency) -> (module)
// A < B
// A < C
// B < D
// C < D

// Output: (just need to output any one of below)
// A, B, C, D
// A, C, B, D