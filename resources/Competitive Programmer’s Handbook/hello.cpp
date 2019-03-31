#include<iostream>
#include<set>
using namespace std;

int main(){

    set<int> s;
s.insert(1);
s.insert(2);
s.insert(2);
s.insert(3);
s.insert(6);
s.insert(6);
s.insert(8);


    auto it = s.lower_bound(x);
    if (it == s.begin()) {
    cout << *it << "\n";
    } else if (it == s.end()) {
    it--;
    cout << *it << "\n";
    } else {
    int a = *it; it--;
    int b = *it;
    if (x-b < a-x) cout << b << "\n";
    else cout << a << "\n";
    }

    return 0;
}
