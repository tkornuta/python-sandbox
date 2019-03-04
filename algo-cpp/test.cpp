#include <iostream>
#include <map>

using namespace std;

int main(){
    std::map <int, string> mymap;
    int a = 12;
    //cin >> a;
    mymap.insert(std::pair<int, string>(10, "ala"));
    cout << mymap.size() << endl;

    for (auto &kv: mymap)
        cout << kv.first << endl;
}
