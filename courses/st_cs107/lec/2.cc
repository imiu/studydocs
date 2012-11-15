#include <iostream>
using namespace std;

int main() {
  char ch = 'A';
  short s = ch;
  cout << s << endl;

  short ss = 67;
  char chh = ss;
  cout << chh << endl;

  int i = 16809984; // 2^24 + 2^15
  short sss = i;
  cout << sss << endl;

  int ii = 5;
  float f = ii;
  cout << f << endl;

  int iii = 37;
  float ff = *(float*) &iii;
  cout << ff << endl;

  float fff = 7.0;
  short ssss = *(short*) &fff;
  cout << ssss << endl;

  return 0;
}
