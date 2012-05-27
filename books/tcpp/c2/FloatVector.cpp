#include <vector>
#include <iostream>
using namespace std;

int main() {
    vector<float> v1;
    vector<float> v2;
    vector<float> vs;

    vector<float> vsq;

    for (int i = 0; i < 5; i++) {
        v1.push_back(0.5 + i);
    }

    for (int i = 0; i < 5; i++) {
        v2.push_back(0.2 + i);
    }

    for (int i = 0; i < 5; i++) {
        vs.push_back(v1[i] + v2[i]);
    }

    for (int i = 0; i < 5; i++) {
        cout << v1[i] << " " << endl;
    }

    for (int i = 0; i < 5; i++) {
        cout << v2[i] << " " << endl;
    }

    for (int i = 0; i < 5; i++) {
        cout << vs[i] << " " << endl;
    }

    for (int i = 0; i < 5; i++) {
        vsq.push_back(0.5 + i);
    }

    cout << "Squares" << endl;

    for (int i = 0; i < vsq.size(); i++) {
        cout << vsq[i] << " ";
    }
    cout << endl;

    for (int i = 0; i < vsq.size(); i++) {
        vsq[i] = vsq[i] * vsq[i];
    }

    for (int i = 0; i < vsq.size(); i++) {
        cout << vsq[i] << " ";
    }
    cout << endl;

}
