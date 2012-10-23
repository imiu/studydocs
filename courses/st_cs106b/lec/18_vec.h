#ifndef _MyVector_H
#define _MyVector_H
#include <string>
using namespace std;

class MyVector {
    public:
        MyVector();
        ~MyVector();

        int size();
        void add(string s);
        string getAt(int index);

    private:
        string *arr;
        int numUsed;
        int numAllocated;
        void doubleCapacity();
};

#endif
