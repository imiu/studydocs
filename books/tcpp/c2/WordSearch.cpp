#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    ifstream in("tst");
    string search_word;
    string word;
    int swc;

    cout << "Give me a word to search: ";
    cin >> search_word;
    cout << endl;

    while (in >> word) {
        if (word == search_word) {
            swc++;
        }
    }

    cout << "Total searched word count: " << swc << endl;
}

