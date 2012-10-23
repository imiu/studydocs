#include "18_vec_tmp.h"
#include <iostream>
using namespace std;

template <typename ElemType>
MyVector<ElemType>::MyVector() {
    arr = new ElemType[10];
    numAllocated = 2;
    numUsed = 0;
}

template <typename ElemType>
MyVector<ElemType>::~MyVector() {
    delete[] arr;
}

template <typename ElemType>
int MyVector<ElemType>::size() {
    return numUsed;
}

template <typename ElemType>
ElemType MyVector<ElemType>::getAt(int index) {
    if (index < 0 || index >= size()) {
        cout << "Dead" << endl;
    }
    return arr[index];
}

template <typename ElemType>
void MyVector<ElemType>::add(ElemType s) {
    if (numUsed == numAllocated) {
        doubleCapacity();
    }
    arr[numUsed++] = s;
}

template <typename ElemType>
void MyVector<ElemType>::doubleCapacity() {
    ElemType *bigger = new ElemType[numAllocated * 2];
    for (int i = 0; i < numUsed; i++) {
        bigger[i] = arr[i];
    }

    delete[] arr;
    arr = bigger;
    numAllocated *= 2;
}
