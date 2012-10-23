#include <iostream>
#include "18_vec.h"

int main() {
    MyVector v;
    v.add("lazar");
    v.add("more");
    v.add("more");
    v.add("more");
    v.add("more");
    v.add("some");

    for (int i = 0; i < v.size(); i++) {
        cout << v.getAt(i) << endl;
    }

    return 0;
}
