#include <iostream>

// Int search
int isearch(int key, int array[], int size) {
  for (int i = 0; i < size; i++) {
    if (array[i] == key) {
      return i;
    }
  }
  return -1;
}

void *lsearch(void *key, void *base, int n, int elemSize) {
  for (int i = 0; i < n; i++) {
    void *elemAddr = (char *)base + i * elemSize;
    if (memcmp(key, elemAddr, elemSize) == 0) {
      return elemAddr;
    }
  }
  return NULL;
}

void *llsearch(void *key, void *base, int n, int elemSize,
    int (*cmpfn)(void*, void*)) {

}

int main() {

}
