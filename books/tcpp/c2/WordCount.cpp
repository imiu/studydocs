#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    ifstream in("tst");
    string word;
    int wc;

    while (in >> word) {
        wc++;
    }

    cout << "Total word count: " << wc << endl;
}

