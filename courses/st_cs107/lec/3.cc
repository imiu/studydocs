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

// Structs with arrays
struct student {
  char *name; // Will be stored outside of struct
  char suid[8];
  int numUnits;
  friend ostream& operator<< (ostream &o, const student &f) {
    return o << "name = " << f.name << endl
      << "suid = " << f.suid << endl
      << "numUnits = " << f.numUnits << endl;
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

  unsigned short bs = 128;
  // Show the actual binary
  bitset<CHAR_BIT * sizeof(short)> bin;
  bin |= bs;
  cout << "LE Binary: " << bin << endl;
  unsigned short ssb = ntohs(bs);
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

  ((fraction *)&(pi.denum))->num=65534; // This change denum actually
  ((fraction *)&(pi.denum))->denum=65535; // Changing outside of struct
  cout << pi << endl;


  // Arrays
  int a[10];
  cout << &a << endl;
  cout << &a[4] << endl;
  // Pointer arithmetic
  cout << (&a[0] + 4) << endl;

  int ar[5];
  ar[3] = 128;
  cout << ar[3] << endl;
  ((short*)ar)[7] = 2;
  cout << ar[3] << endl;

  ((short*)(((char*)(&ar[1])) + 8))[1] = 137;
  cout << ar[3] << endl;

  student pupils[4];
  pupils[0].numUnits = 2;
  pupils[0].name = strdup("Adam");
  pupils[1].name = strdup("Adam");
  pupils[2].name = strdup("Adam");
  pupils[3].name = strdup("Adam");
  pupils[3].name = pupils[0].suid + 6;
  strcpy(pupils[1].suid, "40415xx");
  // strcpy(pupils[3].name, "123456");

  for (int i = 0; i < 3; i++) {
    cout << pupils[i];
  }
}
