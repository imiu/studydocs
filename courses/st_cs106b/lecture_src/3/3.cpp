/*
 *  3.cpp
 *  3
 *
 *  Created by Alexander Kudryashov on 13.08.2010.
 *  Copyright 2010 Qbero. All rights reserved.
 *
 */

#include "3.h"
#include "genlib.h"
#include <iostream>

void RemoveOccurrences(char ch, string &s) {
    int found = 0;
    while ((found = s.find(ch, found)) != string::npos) {
        s.erase(found, 1);
    }
}

int main() {
    string s = "chuhuahua chese crackers";
    RemoveOccurrences('c', s);
    cout << s << endl;
    
    return 0;
}