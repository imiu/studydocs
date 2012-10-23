#include "18_vec.h"
#include <iostream>
using namespace std;

MyVector::MyVector() {
    arr = new string[10];
    numAllocated = 2;
    numUsed = 0;
}

MyVector::~MyVector() {
    delete[] arr;
}

int MyVector::size() {
    return numUsed;
}

string MyVector::getAt(int index) {
    if (index < 0 || index >= size()) {
        cout << "Dead" << endl;
    }
    return arr[index];
}

void MyVector::add(string s) {
    if (numUsed == numAllocated) {
        doubleCapacity();
    }
    arr[numUsed++] = s;
}

void MyVector::doubleCapacity() {
    string *bigger = new string[numAllocated * 2];
    for (int i = 0; i < numUsed; i++) {
        bigger[i] = arr[i];
    }

    delete[] arr;
    arr = bigger;
    numAllocated *= 2;
}
