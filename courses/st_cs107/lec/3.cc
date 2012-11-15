#include <iostream>
#include <bitset>
using namespace std;
// Struct
struct fraction {
  unsigned short num;
  unsigned short denum;
  fraction(short int num_, short int denum_):
    num(num_), denum(denum_) {}
  friend ostream& operator<< (ostream &o, const fraction &f) {
    return o << "num   = " << f.num << endl
      << "denum = " << f.denum << endl;
  }
};

int main() {
  // Endianess
  unsigned short s;
  unsigned char c;

  s = 0x0001;
  c = *(unsigned char *) (&s);
  if(c == 0x01) {
    cout << "LE" << endl;
  } else {
    cout << "BE" << endl;
  }


  // Show the actuall binary
  bitset<CHAR_BIT * sizeof(short)> bin;
  bin |= s;
  cout << "LE Binary: " << bin << endl;
  unsigned short ssb = ntohs(s);
  bin.reset();
  bin |= ssb;
  unsigned short bes = (unsigned short)bin.to_ulong();
  cout << "LE as BE Short: " << ssb << endl;

  unsigned short ss = htons(s);
  bin.reset();
  bin |= ss;
  cout << "BE Binary: " << bin << endl;
  unsigned short les = (unsigned short)bin.to_ulong();
  cout << "BE as LE Short: " << ssb << endl;

  // Structs
  cout << endl;
  fraction pi(65533, 65533);
  cout << pi << endl;
  cout << &pi << endl;
  cout << &pi.denum << endl;
  cout << &((fraction *)&(pi.denum))->denum << endl;

  ((fraction *)&(pi.denum))->num=65535; // This change denum actually
  ((fraction *)&(pi.denum))->denum=65535; // Changing outside of struct
  cout << pi << endl;
}
