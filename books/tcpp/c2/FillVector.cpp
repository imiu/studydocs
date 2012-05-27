#include <string>
#include <vector>
#include <fstream>
#include <iostream>
using namespace std;

int main() {
    vector<string> v;
    ifstream in("Fillvector.cpp");
    string line;
    string all_lines;
    int tot;

    while (getline(in, line)) {
        v.push_back(line);
    }

    // Natural order
    for (int i = 0; i < v.size(); i++) {
        cout << i << ": " << v[i] << endl;
    }

    // Reverse order
    for (int i = v.size() - 1; i >= 0; i--) {
        cout << i << ": " << v[i] << endl;
    }

    // All lines
    for (int i = 0; i < v.size(); i++) {
        all_lines += v[i] + "\n";
    }

    cout << all_lines;

    // Use interaction
    string c;
    for (int i = 0; i < v.size(); i++) {
        cout << v[i] << endl;
        getline(cin, c);
    }
}
