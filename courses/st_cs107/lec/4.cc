#include <iostream>
using namespace std;

// Int swap
void iswap(int *ap, int *bp) {
  int temp = *ap;
  *ap = *bp;
  *bp = temp;
}

// General swap
void swap(void *vp1, void *vp2, int size) {
  char buffer[size];
  memcpy(buffer, vp1, size);
  memcpy(vp1, vp2, size);
  memcpy(vp2, buffer, size);
}

int main() {
  cout << "Swap the pointers" << endl;
  int *a = new int();
  int *b = new int();
  *a = 128;
  *b = 256;
  cout << "Address a = " << a << endl;
  cout << "Value   a = " << *a << endl;
  cout << "Address b = " << b << endl;
  cout << "Value   b = " << *b << endl;

  swap(a, b, sizeof(int *));
  cout << "Address a = " << a << endl;
  cout << "Value   a = " << *a << endl;
  cout << "Address b = " << b << endl;
  cout << "Value   b = " << *b << endl;
  delete a;
  delete b;

  cout << endl;
  cout << "Swap the values" << endl;
  int c = 128;
  int d = 256;
  cout << "Address c = " << &c << endl;
  cout << "Value   c = " << c << endl;
  cout << "Address d = " << &d << endl;
  cout << "Value   d = " << d << endl;

  swap(&c, &d, sizeof(int));
  cout << "Address c = " << &c << endl;
  cout << "Value   c = " << c << endl;
  cout << "Address d = " << &d << endl;
  cout << "Value   d = " << d << endl;

  cout << endl;
  cout << "Passing the &pointers" << endl;
  char *h = strdup("Fred");
  char *w = strdup("Wilma");
  cout << "Address h = " << &h << endl;
  cout << "Value   h = " << h << endl;
  cout << "Address w = " << &w << endl;
  cout << "Value   w = " << w << endl;

  swap(&h, &w, sizeof(char *));
  cout << "Address h = " << &h << endl;
  cout << "Value   h = " << h << endl;
  cout << "Address w = " << &w << endl;
  cout << "Value   w = " << w << endl;

  cout << endl;
  cout << "Passing the pointers" << endl;

  swap(h, w, sizeof(char *));
  cout << "Address h = " << &h << endl;
  cout << "Value   h = " << h << endl;
  cout << "Address w = " << &w << endl;
  cout << "Value   w = " << w << endl;

}
