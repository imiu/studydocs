/*
 *  average.cpp
 *  2
 *
 *  Created by Alexander Kudryashov on 13.08.2010.
 *  Copyright 2010 Qbero. All rights reserved.
 *
 */

#include "genlib.h"
#include <iostream>
#include "simpio.h"

double GetScoresAndAverage(int sentinel = -1);

int main() {
    cout << "Welcome" << endl;
    double average = GetScoresAndAverage();
    cout << "Average is " << average << endl;
    return 0;
}

double GetScoresAndAverage(int sentinel) {
    int sum = 0;
    int cnt = 0;
    int value;
    
    while (true) {
        cout << "Next? ";
        value = GetInteger();
        if (value == sentinel) break;
        sum += value;
        cnt++;            
    }
    return double(sum) / cnt;
}