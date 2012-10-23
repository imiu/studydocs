#ifndef _MyVector_H
#define _MyVector_H
#include <string>
using namespace std;

template <typename ElemType>
class MyVector {
    public:
        MyVector();
        ~MyVector();

        int size();
        void add(ElemType s);
        ElemType getAt(int index);

    private:
        ElemType *arr;
        int numUsed;
        int numAllocated;
        void doubleCapacity();
};

#include "18_vec_tmp.cc"

#endif
