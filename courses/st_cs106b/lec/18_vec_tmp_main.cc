#include <iostream>
#include "18_vec_tmp.h"

int main() {
    MyVector<string> v;
    v.add("lazar");
    v.add("more");
    v.add("more");
    v.add("more");
    v.add("more");
    v.add("some");
    for (int i = 0; i < v.size(); i++) {
        cout << v.getAt(i) << endl;
    }

    MyVector<int> vv;
    vv.add(1);
    vv.add(1);
    vv.add(1);
    vv.add(1);
    vv.add(1);
    vv.add(1);
    for (int i = 0; i < vv.size(); i++) {
        cout << vv.getAt(i) << endl;
    }


    return 0;
}
